import unittest, os
from pymodm import connect
from models import Hiker, Trails, Location, Comment
import pymongo
from app import app
from bson.objectid import ObjectId


app.config['DEBUG'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED']= False
app.testing = True
app.secret_key = os.environ.get("API_SECRET")
MONGODB_URI = os.environ.get('MONGO_URI')

testTrailName = 'The Great Sugar Loaf Trail'

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    def test_routes(self):
        response = self.app.get('/',follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/directory')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/top-rated')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/create_profile')
        self.assertEqual(response.status_code, 200)

        trails = Trails.objects.get({'trail_name': testTrailName})
        response = self.app.get('/trails/'+str(trails._id))
        self.assertEqual(response.status_code, 200)
        
    """
    Test if valid user registration
    """
    def register(self, username, fname, lname, origin, email, trails_completed, profile_pic):
        return self.app.post('/create_profile', data=dict(
            username=username, fname=fname, lname=lname, origin=origin, email=email, trails_completed=trails_completed, profile_pic=profile_pic), follow_redirects=True)

    #def test_valid_user_registration(self):
    #    response = self.register('ttester1', 'test', 'tester', 'QADept', 'test@tester.com', 100, 'http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg')
    #    self.assertEqual(response.status_code, 200)
    #    success_msg = "Profile Created Successfully"
    #    self.assertIn(str.encode(success_msg), response.data)
    #     document = BeautifulSoup(response.data, features='html.parser')
    #     assert document.find("div", {"class" : "parallax-container"})

    """
    Test if user register with an invalid username
    """
    def test_invalid_user_registration_duplicate_username(self):
        response = self.register('ttester1', 'pied', 'piper', 'USA', 'pied@piper.com', 10, 'http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg')
        self.assertEqual(response.status_code, 200)
        error_msg = "User already exists. Please choose another username."
        self.assertIn(str.encode(error_msg), response.data)

    """
    Test if user register with an invalid e-mail address
    """
    def test_user_registration_invalid_email(self):
        response = self.register('iamtester', 'pied', 'pipper', 'USA', 'abcde.12345@gemailcom', 0, 'http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg')
        error_msg = "Not a valid e-mail address"
        
    def login(self, username, email):
        return self.app.post(
            '/login',
            data=dict(username=username, email=email),
            follow_redirects=True
        )

    def test_valid_user_login(self):
        response = self.login('ttester1', 'pied@piper.com')
        self.assertEqual(response.status_code, 200)
        success_msg = "You logged in successfully as ttester1"
        self.assertIn(str.encode(success_msg), response.data)
        
    def deregister():
        pass

if __name__ == '__main__':
    unittest.main()