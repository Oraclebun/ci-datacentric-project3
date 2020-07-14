from flask import Flask, render_template, request, redirect, url_for
from models import Hiker, Trails, Location, Comment
import os

app = Flask(__name__)

@app.route('/')
def index():
    all_trails = Trails.objects.values().all()
    all_trail_loc = Trails.objects.only('location')
    print(all_trails)
    return "Test display"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)