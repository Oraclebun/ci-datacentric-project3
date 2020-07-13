import os
import datetime
from dotenv import load_dotenv
from pymodm import connect, fields, MongoModel, EmbeddedDocumentListField

load_dotenv()

MONGODB_URI = os.environ.get('MONGO_URI')

# Connect to MongoDB first. PyMODM supports all URI options supported by
# PyMongo. Specify a database in the connection string:
connect(MONGODB_URI)

# Use pymodm to manage collection in database
# Models Definition


class Hiker(MongoModel):
    """
    A model defining hiker, with hiker attribute, first name, last name, country of origin and e-mail.
    Profile pic is a url field that stores the link to the hiker's profile photo.
    Trails completed refers to the no of trails completed by hiker currently.
    """
    fname = fields.CharField(min_length=2, max_length=30)
    lname = fields.CharField(max_length=20)
    username = fields.CharField(min_length=5, max_length=20)
    origin = fields.CharField(max_length=30)
    email = fields.EmailField()
    trails_completed = fields.IntegerField(min_value=0)
    profile_pic = fields.URLField(
        default="https://res.cloudinary.com/c7oud0311/image/upload/v1594654152/project3/profile2_vcog5c.jpg")

    def __str__(self):
        return f'{self.fname}({self.lname})'
