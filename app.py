from flask import Flask, render_template, request, redirect, url_for, flash
from models import Hiker, Trails, Location, Comment
import os
import pymongo
import hashlib
import flask_login
from dotenv import load_dotenv
from bson.objectid import ObjectId
from forms import CreateProfile, LoginForm
from pymodm import connect

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
        print(user_in_db)
        user = User()
        # set the id of the user object to be the user's email
        user.id = user_in_db._id
        return user
    except Hiker.DoesNotExist:
        return None


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


@app.route('/')
def index():
    comments = Trails.objects.order_by(
        [('comments.date_comment', pymongo.DESCENDING)])
    all_comm = list(comments.only('comments'))
    all_trails = Trails.objects.values().all()
    all_trail_loc = Trails.objects.only('location')
    trails_loc = []
    reviews = []
    for i in range(3):
        comments = {
            'author': all_comm[i:(i+1)][0].comments[0].author.fname+' '+all_comm[i:(i+1)][0].comments[0].author.lname,
            'photo': all_comm[i:(i+1)][0].comments[0].author.profile_pic,
            'body': all_comm[i:(i+1)][0].comments[0].body,
            'date': all_comm[i:(i+1)][0].comments[0].date_comment.strftime("%d-%b-%Y"),
            'track': Trails.objects.get({'_id': all_comm[i:i+1][0]._id}),
            'country': Trails.objects.get({'_id': all_comm[i:i+1][0]._id}).location.country
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
    return render_template('index.html', location=trails_loc, comments=reviews)


@app.route('/trails/<trail_id>')
def get_trail(trail_id):
    trail = Trails.objects.get({'_id': ObjectId(trail_id)})
    return render_template('trails/trails.template.html', trail=trail)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #form.db_user.data = user_loader
    if form.validate_on_submit():
        try:
            db_user = Hiker.objects.get({"username": form.username.data})
            if db_user:
                user = User()
                user.id = db_user._id
                if (db_user.email == form.email.data):
                    flask_login.login_user(user)
                    flash(f" You logged in successfully as {db_user.username}")
                    return redirect(url_for('index'))
                else:
                    flash(f" Wrong e-mail address")
                    return render_template('trails/403_error.html', error = "Forbidden")
        except Hiker.DoesNotExist:
            return 'Login Failed, Please register'
    return render_template('trails/login.template.html', form=form)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return "logged out"

""" 
Route to show user profiles.
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
        return redirect(url_for('index'))
    return render_template('trails/create_profile.template.html', form=form, cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET, api_key=API_KEY)

"""
Route to edit profile
"""
@flask_login.login_required
@app.route('/profiles/edit/<hiker_id>', methods=['GET', 'POST'])
def edit_profile(hiker_id):
    profile_to_edit = Hiker.objects.get({'_id': ObjectId(hiker_id)})
    form = CreateProfile(obj=profile_to_edit)
    if form.validate_on_submit():
        try:
            Hiker.objects.raw({"_id": ObjectId(hiker_id)}).update({"$set": {"fname": form.fname.data,
                                                                            "lname": form.lname.data,
                                                                            "origin": form.origin.data,
                                                                            "email": form.email.data,
                                                                            "trails_completed": form.trails_completed.data,
                                                                            "profile_pic":form.profile_pic.data
                                                                            }}, upsert=False)
        except ValidationError as ve:
            errors = ve.message
        return redirect(url_for('index'))
    return render_template('trails/edit_profile.template.html', form=form, profileId=profile_to_edit._id, cloud_name=CLOUD_NAME,
                           upload_preset=UPLOAD_PRESET, api_key=API_KEY)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
