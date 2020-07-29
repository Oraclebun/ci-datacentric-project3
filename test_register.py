import unittest
import os
from models import Hiker, Trails, Location, Comment
import pymongo
from app import app
from bson.objectid import ObjectId
from bs4 import BeautifulSoup
import re

app.config['DEBUG'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.testing = True
app.secret_key = os.environ.get("API_SECRET")
MONGODB_URI = os.environ.get('MONGO_URI')

testTrailName = 'The Great Sugar Loaf Trail'


class TestReg(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    """
    Test if valid user registration
    """

    def register(self, username, fname, lname, origin, email,
                 trails_completed, profile_pic):
        return self.app.post('/create_profile', data=dict(
            username=username, fname=fname, lname=lname, origin=origin,
            email=email, trails_completed=trails_completed,
            profile_pic=profile_pic), follow_redirects=True)

    def test_valid_user_registration(self):
        response = self.register('ttester1', 'Test', 'Tester', 'Japan',
                                 'test@tester.com', 100,
                                 'http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg')
        self.assertEqual(response.status_code, 200)
        success_msg = "Registration Successful."
        self.assertIn(str.encode(success_msg), response.data)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("div", {"class": "parallax-container"})


if __name__ == '__main__':
    unittest.main()
