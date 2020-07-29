from flask import Flask, render_template, request, redirect, url_for, session, flash, Markup
from models import Hiker, Trails, Location, Comment
import os
import pymongo
import hashlib
import datetime
import flask_login
from dotenv import load_dotenv
from bson.objectid import ObjectId
from forms import CreateProfile, UpdateProfile, CommentsForm
from pymodm import connect
from pymodm.errors import ValidationError

load_dotenv()

MONGODB_URI = os.environ.get('MONGO_URI')
SECRET_KEY = os.environ.get("SECRET_KEY")

# Connect to MongoDB first. PyMODM supports all URI options supported by
# PyMongo. Specify a database in the connection string:
connect(MONGODB_URI)

app = Flask(__name__)
app.secret_key = SECRET_KEY
CLOUD_NAME = os.environ.get("CLOUD_NAME")
UPLOAD_PRESET = os.environ.get("UPLOAD_PRESET")
API_SECRET = os.environ.get("API_SECRET")
API_KEY = os.environ.get("API_KEY")

# Create the login manager
login_manager = flask_login.LoginManager()
#
login_manager.init_app(app)

# get the user object from flask-login mixin
class User(flask_login.UserMixin):
    pass

# user loader for the Flask-Login login manager

@login_manager.user_loader
def user_loader(id):
    try:
        # find the user from the database by its username
        user_in_db = Hiker.objects.get({"_id": ObjectId(id)})
        user = User()
        # set the id of the user object to be the user's email
        user.id = user_in_db._id
        return user
    except Hiker.DoesNotExist:
        return None


"""
Signature generator for signed image upload to cloudinary
The compute_hex_hash and api_sign_request is taken from
cloudinary-django
"""


def compute_hex_hash(s):
    """
    Compute hash and convert the result to HEX string
    :param s: string to process
    :return: HEX string
    """
    return hashlib.sha1(str(s).encode('utf-8')).hexdigest()


def api_sign_request(params_to_sign, api_secret):
    params = [(k + "=" + (",".join(v) if isinstance(v, list) else str(v)))
              for k, v in params_to_sign.items() if v]
    to_sign = "&".join(sorted(params))
    return compute_hex_hash(to_sign + api_secret)


@app.route('/generateKey')
def signUploadRequest():
    params_to_sign = request.args.to_dict()
    signature = api_sign_request(params_to_sign, API_SECRET)
    return {"signature": signature}


""" 
Route to show homepage
"""
@app.route('/')
def index():
    qs = Trails.objects.raw({})
    cursor = qs.aggregate(
        {
            "$unwind": "$comments"
        },
        {"$lookup":
         {
             "from": "hiker",
             "localField": "comments.author",
             "foreignField": "_id",
             "as": "hiker"
         }
         },
        {
            "$sort": {
                "comments.date_comment": pymongo.DESCENDING
            }
        },
        {"$lookup":
         {
             "from": "location",
             "localField": "location",
             "foreignField": "_id",
             "as": "location"
         }
         },
        {"$unwind": "$location"},
        {"$unwind": "$hiker"},
        {
            "$project": {
                "trail_name": 1,
                "location.country": 1,
                "hiker.fname": 1,
                "hiker.lname": 1,
                "hiker.profile_pic": 1,
                "comments.body": 1,
                "comments.date_comment": 1
            }
        }
    )

    all_reviews = list(cursor)[0:3]
    all_trail_loc = Trails.objects.only('location')
    trails_loc = []
    reviews = []
    for attr in all_reviews:
        comments = {
            '_id': attr['_id'],
            'author': attr['hiker']['fname']+' '+attr['hiker']['lname'],
            'photo': attr['hiker']['profile_pic'],
            'body': attr['comments']['body'],
            'date': attr['comments']['date_comment'].strftime("%d-%b-%Y"),
            'trail_name': attr['trail_name'],
            'country': attr['location']['country']
        }
        reviews.append(comments)
    for loc in all_trail_loc:
        locations = {
            'trail_id': loc._id,
            'trail_name': Trails.objects.get({'_id': loc._id}).trail_name,
            'country': loc.location.country,
            'province': loc.location.province[0].state,
            'town': loc.location.province[0].town.town
        }
        trails_loc.append(locations)
    auth_user=session.get('_user_id')
    return render_template('index.html', location=trails_loc, comments=reviews, auth_user=auth_user)


""" 
Route to show all trails (searchable) in database as a directory
"""
@app.route('/directory')
def show_all():
    auth_user = session.get('_user_id')
    search_terms = request.args.get('query')
    route_types = request.args.getlist('route-type')
    route_regex = "|".join(route_types)
    difficulties = request.args.getlist('difficulty')
    difficulty_regex = "|".join(difficulties)
    qs = Trails.objects.raw({})

    # if there are search terms and the lists are not empty
    if (search_terms != "" and search_terms is not None) or (route_types) or (difficulties):
        cursor = qs.aggregate(
            {"$lookup":
             {
                 "from": "location",
                 "localField": "location",
                 "foreignField": "_id",
                 "as": "location"
             }
             },
            {"$match": {
                "$and":[{
                "$or": [
                    {"location.country": {"$regex": search_terms, "$options": 'i'}},
                    {"location.province.state": {
                        "$regex": search_terms, "$options": 'i'}},
                    {"location.province.town.town": {
                        "$regex": search_terms, "$options": 'i'}},
                    {"location.town": {"$regex": search_terms, "$options": 'i'}},
                    {"trail_name": {"$regex": search_terms, "$options": 'i'}},
                    {"distance": {"$regex": search_terms, "$options": 'i'}},
                    {"description": {"$regex": search_terms, "$options": 'i'}}
                ]},
                {
                "$or": [
                    {"route_type": {"$regex": route_regex, "$options": 'i'}}
                ]},
                {
                "$or": [
                    {"difficulty": {"$regex": difficulty_regex, "$options": 'i'}}
                ]}
                ]
            }
            },
            {"$unwind": "$location"},
            {"$unwind": "$location.province"},
            {"$unwind": "$location.province.town"}
        )
    else:
        cursor = qs.aggregate(
            {"$lookup":
             {
                 "from": "location",
                 "localField": "location",
                 "foreignField": "_id",
                 "as": "location"
             }
             },
            {"$unwind": "$location"},
            {"$unwind": "$location.province"},
            {"$unwind": "$location.province.town"}
        )
    return render_template('trails/directory.template.html', all_trails=cursor, auth_user = auth_user)


""" 
Route to show trail in database sorted by average user ratings
"""
@app.route('/top-rated')
def show_by_rating():
    auth_user= session.get('_user_id')
    qs = Trails.objects.raw({})
    cursor = qs.aggregate(
            {"$addFields": {
                "avrg_rating": {"$avg": "$comments.ratings"}        #add a new field that average all ratings
            }},
            {"$addFields": {
                "rating_average": {"$round": ["$avrg_rating",0]}    #add a new field that rounds the average ratings
            }},
            {"$lookup":
             {
                 "from": "location",
                 "localField": "location",
                 "foreignField": "_id",
                 "as": "location"
             }
             },
            {"$unwind": "$location"},
            {"$unwind": "$location.province"},
            {"$unwind": "$location.province.town"},
            {"$project": {
                "_id": 1,
                "trail_name": 1,
                "description": 1,
                "image": 1,
                "embed_route": 1,
                "distance": 1,
                "route_type": 1,
                "elevation": 1,
                "difficulty": 1,
                "centrepoint": 1,
                "waypoints": 1,
                "location": 1,
                "rating_average": {"$ifNull": ['$rating_average', 0]}    
            }
            },
            {
                "$group":{
                    "_id": "$rating_average",
                    "trails": { "$push": "$$ROOT" }
                }
            },
            {
                "$sort": {
                    "_id": pymongo.DESCENDING
                }
            }
        )

    return render_template('trails/top_rated.template.html', rated=cursor, auth_user=auth_user)


""" 
Route to show trail in database and it's comments
"""
@app.route('/trails/<trail_id>')
def get_trail(trail_id):
    pre_q = Trails.objects.raw({
        '$and': [
            {
            "_id": ObjectId(trail_id)
            },
            {'comments': {'$exists': True, '$not': {'$size': 0 }}},
        ]
    })

    qs = Trails.objects.raw({'_id': ObjectId(trail_id)})
    if not list(pre_q):
        cursor = qs.aggregate(
            {"$addFields": {
                "rating_average": {"$avg": "$comments.ratings"}
            }},
            {"$project": {
                "_id": 1,
                "trail_name": 1,
                "description": 1,
                "embed_route": 1,
                "image": 1,
                "distance": 1,
                "route_type": 1,
                "elevation": 1,
                "difficulty": 1,
                "centrepoint": 1,
                "waypoints": 1,
                "location": 1,
                "rating_average": {"$ifNull": ['$rating_average', 0]}
            }
            }
        )
    else:
        cursor = qs.aggregate(
            {"$addFields": {
                "rating_average": {"$avg": "$comments.ratings"}
            }},
            {
                "$unwind": "$comments"
            },
            {
                "$sort": {
                    "comments.date_comment": pymongo.DESCENDING
                }
            },
            {"$lookup":
             {
                 "from": "hiker",
                 "localField": "comments.author",
                 "foreignField": "_id",
                 "as": "comments.author"
             }
             },
            {
                "$unwind": "$comments.author"
            },
            {
                "$group": {
                    "_id": "$_id",
                    "trail_name": {"$first": "$trail_name"},
                    "description": {"$first": "$description"},
                    "embed_route": {"$first": "$embed_route"},
                    "image": {"$first": "$image"},
                    "distance": {"$first": "$distance"},
                    "route_type": {"$first": "$route_type"},
                    "elevation": {"$first": "$elevation"},
                    "difficulty": {"$first": "$difficulty"},
                    "centrepoint": {"$first": "$centrepoint"},
                    "waypoints": {"$first": "$waypoints"},
                    "location": {"$first": "$location"},
                    "rating_average": {"$first": "$rating_average"},
                    "comments": {"$push": "$comments"}
                }
            },
            {"$project": {
                "_id": 1,
                "trail_name": 1,
                "description": 1,
                "embed_route": 1,
                "image":1,
                "distance": 1,
                "route_type": 1,
                "elevation": 1,
                "difficulty": 1,
                "centrepoint": 1,
                "waypoints": 1,
                "location": 1,
                "rating_average": 1,
                "comments": 1
            }
            }
        )
    trails = []
    for results in cursor:
        dictionary = {
            '_id': results['_id'],
            'trail_name': results['trail_name'],
            'distance': results['distance'],
            'elevation': results['elevation'],
            'route_type': results['route_type'],
            'difficulty': results['difficulty'],
            'description': results['description'],
            'waypoints': results['waypoints'],
            'centrepoint': results['centrepoint'],
            'image': results['image'],
            'embed_route': Markup(results['embed_route']),
            'location': results['location'],
            'avg_rating': results['rating_average'],
            'comments': results.get("comments", [])
        }
        trails.append(dictionary)
    
    auth_user = session.get('_user_id')  #for nav bar profile button
    authenticated_user = ObjectId(session.get('_user_id'))
    return render_template('trails/trails.template.html', trails=trails, auth_user=auth_user, authenticated_user=authenticated_user)


""" 
Route to login user.
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    auth_user= session.get('_user_id')
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        try:
            db_user = Hiker.objects.get({"username": username})
            if db_user:
                user = User()
                user.id = db_user._id
                if (db_user.email == email):
                    flask_login.login_user(user)
                    flash(f" You logged in successfully as {db_user.username}", 'teal')
                    return redirect(url_for('index'))
                else:
                    flash(f" Wrong e-mail address. Please try again.", 'deep-orange darken-3')
        except Hiker.DoesNotExist:
            flash(f" Wrong username. Please try again.", 'deep-orange darken-3')
    return render_template('trails/login.template.html', auth_user=auth_user)


""" 
Route to logout user.
"""
@app.route('/logout')
def logout():
    flask_login.logout_user()
    flash('You logged out successfully.', 'teal')
    auth_user= session.get('_user_id')
    return render_template('trails/login.template.html', auth_user=auth_user)


""" 
Route to show user profiles.
Route only accessible if user is logged in.
"""
@app.route('/profile')
@flask_login.login_required
def show_profile():
    user = flask_login.current_user
    profile = Hiker.objects.get({'_id': user.id})
    return render_template('trails/profile.template.html', profile=profile)


"""
Route to create profile. 
1. If method = GET, create form from CreateProfile class in form.py
2. If form validated, save profile information into Database
3. Show homepage if form is validated
"""
@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    auth_user = session.get('_user_id')
    form = CreateProfile()
    if form.validate_on_submit():
        Hiker(fname=form.fname.data,
              lname=form.lname.data,
              username=form.username.data,
              origin=form.origin.data,
              email=form.email.data,
              trails_completed=form.trails_completed.data,
              profile_pic=form.profile_pic.data
              ).save()
        flash("Registration Successful.", 'teal')
        return redirect(url_for('index'))
    else:
        if form.errors:
            message = [v for k, v in form.errors.items()]
            flash(message, 'deep-orange darken-3')
    return render_template('trails/create_profile.template.html', form=form, cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET, api_key=API_KEY, auth_user=auth_user)


"""
Route to edit profile
1. If method = GET, populate CreateProfile form from form.py
2. If form validated, save profile information into Database
3. Show homepage if form is validated
"""
@app.route('/profiles/edit/<hiker_id>', methods=['GET', 'POST'])
@flask_login.login_required
def edit_profile(hiker_id):
    profile_to_edit = Hiker.objects.get({'_id': ObjectId(hiker_id)})
    form = UpdateProfile(obj=profile_to_edit)
    if form.validate_on_submit():
        try:
            Hiker.objects.raw({"_id": ObjectId(hiker_id)}).update({"$set": {"fname": form.fname.data,
                                                                            "lname": form.lname.data,
                                                                            "origin": form.origin.data,
                                                                            "email": form.email.data,
                                                                            "trails_completed": form.trails_completed.data,
                                                                            "profile_pic":form.profile_pic.data
                                                                            }}, upsert=False)
            flash("Profile Updated Successfully.", 'teal')
            return redirect(url_for('index'))
        except ValidationError as ve:
            errors = ve.message
            flash(errors, 'deep-orange darken-3')
    return render_template('trails/edit_profile.template.html', form=form, profile=profile_to_edit, cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET, api_key=API_KEY)


"""
Route to delete profile
1. Get all comment objects associated with this profile
2. Pull those objects out of the embedded comments array
3. Log current user out
4. Delete user from database
5. Show homepage if request == 'POST'
"""
@app.route('/profiles/delete/<hiker_id>', methods=['POST'])
@flask_login.login_required
def delete_profile(hiker_id):
    profile_to_delete = Hiker.objects.get({'_id': ObjectId(hiker_id)})
    qs = Trails.objects.raw({})
    cursor = qs.aggregate(
        {
            "$unwind": "$comments"
        },
        {"$lookup":
         {
             "from": "hiker",
             "localField": "comments.author",
             "foreignField": "_id",
             "as": "hiker"
         }
         }
    )

    trail_list=[]
    results = list(cursor)
    for r in results:
        if str(r['comments']['author']) == hiker_id:
            dictionary = {
            '_id': r['_id'],
            'date_comment': r['comments']['date_comment'],
            'body': r['comments']['body'],
            'date_started': r['comments']['date_started'],
            'ratings': r['comments']['ratings'],
            'hours_taken': r['comments']['hours_taken'],
            'minutes_taken': r['comments']['minutes_taken']
            }
            trail_list.append(dictionary)
    
    for each in trail_list:
        Trails.objects.raw({'_id': each['_id']}).update(
                {"$pull": {
                    "comments": {
                        "author": ObjectId(hiker_id),
                        "date_comment": each['date_comment'],
                        "body": each['body'],
                        "date_started": each['date_started'],
                        "ratings": each['ratings'],
                        "hours_taken": each['hours_taken'],
                        "minutes_taken": each['minutes_taken']
                    }
                }
                })

    flask_login.logout_user()
    profile_to_delete.delete()
    flash("Profile Deleted Successfully.", 'teal')
    return redirect(url_for('index'))


"""
Route to add new comment
1. get current logged in user, 
2. get trails object, get user profile, display form
3. if form is validated, try save the comments into the database.
4. if there's an exception, pull the save comment from database
5. flash the error message
"""
@app.route('/trails/new-comments/<trail_id>', methods=['GET', 'POST'])
@flask_login.login_required
def add_comment(trail_id):
    user = flask_login.current_user
    profile = Hiker.objects.get({'_id': user.id})
    current_trail = Trails.objects.get({'_id': ObjectId(trail_id)})
    form = CommentsForm()
    if form.validate_on_submit():
        #sightings = request.form.getlist('sightings')          #enabling this line gets test to work
        sightings = [objects['tag'] for objects in form.sightings.data]
        comment = Comment(
            author=profile,
            date_comment=datetime.datetime.now(),
            body=form.body.data,
            sightings=sightings,
            date_started=form.date_started.data,
            ratings=form.ratings.data,
            hours_taken=form.hours_taken.data,
            minutes_taken=form.minutes_taken.data
        )
        current_trail.comments.append(comment)
        comment_date = comment.date_comment.strftime("%b, %d %Y, %H:%M")
        try:
            current_trail.save()
            flash(f"New comments by '{comment}', on '{comment_date}' have been created", 'teal')
            return redirect(url_for('get_trail', trail_id=trail_id))
        except ValidationError as ve:
            current_trail.comments.pop()
            comment_errors = ve.message['comments'][-1]
            flash(comment_errors, 'deep-orange darken-3')
    return render_template('trails/new_comments.template.html', form=form, current_trail=current_trail)


"""
Route to edit new comment
1. get current logged in user, 
2. check that logged in user is the author of the comment
3. if form is validated, save the comments into the database.
4. Add logic to flash error msg and prevent illegal access to editting comment by non comment owner
"""
@app.route('/trails/edit-comment/<trail_id>/<int:n>', methods=['GET', 'POST'])
@flask_login.login_required
def edit_comment(trail_id, n):
    user = flask_login.current_user
    profile = Hiker.objects.get({'_id': user.id})
    current_trail = Trails.objects.get({'_id': ObjectId(trail_id)})
    comment_to_edit = current_trail.comments[n]
    trail_name = current_trail.trail_name
    if comment_to_edit.author._id != user.id :
        error_msg = "You're not authorized to edit this comment"
        flash(error_msg, 'deep-orange darken-3')
        return redirect(url_for('get_trail', trail_id=trail_id))
    form = CommentsForm(obj=comment_to_edit)
    if form.validate_on_submit():
        print(form.data)
        sightings = [objects['tag'] for objects in form.sightings.data]
        try:
            Trails.objects.raw({'_id': ObjectId(trail_id)}).update(
                {"$set": {
                    "comments."+str(n)+".date_comment": datetime.datetime.now(),
                    "comments."+str(n)+".body": form.body.data,
                    "comments."+str(n)+".sightings": sightings,
                    "comments."+str(n)+".date_started": datetime.datetime.combine(form.date_started.data, datetime.time()),
                    "comments."+str(n)+".ratings": form.ratings.data,
                    "comments."+str(n)+".hours_taken": form.hours_taken.data,
                    "comments."+str(n)+".minutes_taken": form.minutes_taken.data
                }
                })
        except ValidationError as ve:
            current_trail.comments.pop()
            comment_errors = ve.message['comments'][-1]
            flash(comment_errors, 'deep-orange darken-3')
        return redirect(url_for('get_trail', trail_id=trail_id))
    return render_template('trails/edit_comments.template.html', form=form, comment = comment_to_edit, n=n, trail_id=trail_id, trailName = trail_name)


"""
Route to delete comment
1. get current logged in user, 
2. check that logged in user is the author of the comment
3. if he/she/they are the authenticated user, delete the comments from the database
4. else flash the error message
5. return back to the trails view
"""
@app.route('/trails/delete-comment/<trail_id>/<int:n>', methods=['POST'])
@flask_login.login_required
def delete_comment(trail_id, n):
    user = flask_login.current_user
    current_trail = Trails.objects.get({'_id': ObjectId(trail_id)})
    comment_to_delete = current_trail.comments[n]
    try:
        Trails.objects.raw({'_id': ObjectId(trail_id)}).update(
            {"$pull": {
                "comments": {
                    "author": ObjectId(comment_to_delete.author._id),
                    "date_comment": comment_to_delete.date_comment,
                    "body": comment_to_delete.body,
                    "date_started": comment_to_delete.date_started,
                    "ratings": comment_to_delete.ratings,
                    "hours_taken": comment_to_delete.hours_taken,
                    "minutes_taken": comment_to_delete.minutes_taken
                }
            }
            })
        success_msg = "Comment Deleted"
        flash(success_msg, 'teal')
    except ValidationError as ve:
        comment_errors = ve.message
        flash(comment_errors, 'deep-orange darken-3')
    return redirect(url_for('get_trail', trail_id=trail_id))


@app.errorhandler(401)
def page_unauthorized(e):
    return render_template('trails/401_error.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('trails/404_error.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
