import os
import datetime
from dotenv import load_dotenv
from pymodm import connect, fields, MongoModel, EmbeddedMongoModel

load_dotenv()

MONGODB_URI = os.environ.get('MONGO_URI')

# Connect to MongoDB first. PyMODM supports all URI options supported by
# PyMongo. Specify a database in the connection string:
connect(MONGODB_URI)

# Use pymodm to manage collection in database
# Models Definition


class Hiker(MongoModel):
    """
    A model defining hiker, with hiker attribute, first name, last name, 
    country of origin and e-mail. Profile pic is a url field that stores 
    the link to the hiker's profile photo. Trails completed field refers 
    to the no. of trails completed by hiker currently.
    """
    fname = fields.CharField(min_length=2, max_length=30)
    lname = fields.CharField(min_length=2, max_length=20)
    username = fields.CharField(min_length=5, max_length=20)
    origin = fields.CharField(max_length=30)
    email = fields.EmailField()
    trails_completed = fields.IntegerField(min_value=0, default=0)
    profile_pic = fields.URLField(required = True)

    def __str__(self):
        return f'{self.fname}({self.lname})'


class Location(MongoModel):
    """
    A model defining location entity with embedded province and town 
    information.
    """
    country = fields.CharField(max_length=30, required=True)
    province = fields.EmbeddedDocumentListField('Province', required=True)


class Province(EmbeddedMongoModel):
    state = fields.CharField(max_length=30, required=True)
    town = fields.EmbeddedDocumentField('Town', required=True)


class Town(EmbeddedMongoModel):
    town = fields.CharField(max_length=30, required=True)


class Trails(MongoModel):
    """
    A model defining trails entity undertaken by hikers. It has embedded 
    comments which reference the hiker.
    """
    trail_name = fields.CharField(max_length=100, required=True)
    distance = fields.FloatField(max_value=50, required=True)
    elevation = fields.FloatField(required=True)
    route_type = fields.CharField(max_length=20, choices=(
        'Point to Point', 'Loop', 'Out and Back'), required=True)
    difficulty = fields.CharField(max_length=20, choices=(
        'Easy', 'Moderate', 'Difficult'), required=True)
    description = fields.CharField(max_length=500, required=True)
    centrepoint = fields.PointField(required=False)
    waypoints = fields.LineStringField(required=False)
    image = fields.URLField(required = True)
    embed_route = fields.CharField(max_length=800, required=True)
    location = fields.ReferenceField(Location)
    comments = fields.EmbeddedDocumentListField('Comment', required=False)

    def __str__(self):
        return self.trail_name


class Comment(EmbeddedMongoModel):
    """
    A model that defines the reviews entity created by hikers. This 
    model is embedded in each trail.
    """
    author = fields.ReferenceField(Hiker)
    date_comment = fields.DateTimeField(default=datetime.datetime.now())
    body = fields.CharField(max_length=250)
    sightings = fields.ListField(fields.CharField(max_length=20))
    ratings = fields.IntegerField(min_value=1, max_value=5)
    date_started = fields.DateTimeField()
    hours_taken = fields.IntegerField(min_value=0, max_value=48)
    minutes_taken = fields.IntegerField(min_value=0, max_value=59)

    def __str__(self):
        return f'{self.author.fname}{self.author.lname}'
