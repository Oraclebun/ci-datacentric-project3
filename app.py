from flask import Flask, render_template, request, redirect, url_for
from models import Hiker, Trails, Location, Comment
import os
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    comments = Trails.objects.order_by(
        [('comments.date_comment', pymongo.DESCENDING)])
    all_comm=list(comments.only('comments'))
    all_trails = Trails.objects.values().all()
    all_trail_loc = Trails.objects.only('location')
    trails_loc = []
    reviews=[]
    #for t in all_comm:
    #    print(t.comments[0].author, t.comments[0].body)
    for i in range(3):
        comments={
            'author': all_comm[i:(i+1)][0].comments[0].author.fname+' '+all_comm[i:(i+1)][0].comments[0].author.lname,
            'photo' : all_comm[i:(i+1)][0].comments[0].author.profile_pic,
            'body':all_comm[i:(i+1)][0].comments[0].body,
            'date':all_comm[i:(i+1)][0].comments[0].date_comment,
            'track':Trails.objects.get({'_id':all_comm[i:i+1][0]._id}),
            'country':Trails.objects.get({'_id':all_comm[i:i+1][0]._id}).location.country
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
    return render_template('index.html', location = trails_loc, comments=reviews)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)