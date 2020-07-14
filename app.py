from flask import Flask, render_template, request, redirect, url_for
from models import Hiker, Trails, Location, Comment
import os
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    comments = Trails.objects.order_by(
        [('comments.date_comment', pymongo.DESCENDING)])
    all_trails = Trails.objects.values().all()
    all_trail_loc = Trails.objects.only('location')
    trails_loc = []
    for t in comments:
        print(t)
    for loc in all_trail_loc:
        locations = {
            'trail_id': loc._id,
            'trail_name': Trails.objects.get({'_id': loc._id}).trail_name,
            'country': loc.location.country,
            'province': loc.location.province[0].state,
            'town': loc.location.province[0].town.town
        }
        trails_loc.append(locations)
    print(trails_loc)
    return render_template('index.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)