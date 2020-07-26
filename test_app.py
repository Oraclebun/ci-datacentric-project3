import unittest, os
from pymodm import connect
from models import Hiker, Trails, Location, Comment
import pymongo
from app import app
from bson.objectid import ObjectId
from bs4 import BeautifulSoup
from forms import CommentsForm
from flask import request, json
from urllib import request, parse
import re

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

#    def test_valid_user_registration(self):
#        response = self.register('ttester1', 'Test', 'Tester', 'Japan', 'test@tester.com', 100, 'http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg')
#        time.sleep(3)
#        self.assertEqual(response.status_code, 200)
#        success_msg = "Profile Created Successfully"
#        self.assertIn(str.encode(success_msg), response.data)
#        document = BeautifulSoup(response.data, features='html.parser')
#        assert document.find("div", {"class" : "parallax-container"})


    """
    Test if user register with an invalid username
    """
 #   def test_invalid_user_registration_duplicate_username(self):
 #       response = self.register('ttester1', 'Test', 'Tester', 'Japan', 'pied@piper.com', 10, 'http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg')
 #       self.assertEqual(response.status_code, 200)
 #       error_msg = "User already exists. Please choose another username."
 #       self.assertIn(str.encode(error_msg), response.data)
 #       #test form did not submit and page did not redirect
 #       document = BeautifulSoup(response.data, features='html.parser')
 #       assert document.find("form", {"action": "/create_profile"})

    """
    Test if user register with an invalid e-mail address
    """
    def test_user_registration_invalid_email(self):
        response = self.register('iamtester', 'Test', 'Tester', 'Japan', 'abcde.12345@gemailcom', 0, 'http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg')
        error_msg = "Not a valid e-mail address"
        self.assertIn(str.encode(error_msg), response.data)
        #check form did not submit and page did not redirect
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action" : "/create_profile"})


    def login(self, username, email):
        return self.app.post(
            '/login',
            data=dict(username=username, email=email),
            follow_redirects=True
        )

    def test_valid_user_login(self):
        response = self.login('ttester1', 'test@tester.com')
        self.assertEqual(response.status_code, 200)
        success_msg = "You logged in successfully as ttester1"
        self.assertIn(str.encode(success_msg), response.data)
        ### check that page redirected has a div with class=parallax-container(index.html)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("div", {"class" : "parallax-container"})

    
    def test_user_login_invalid_username(self):
        response = self.login('ttester2', 'test@tester.com')
        error_msg = "Wrong username. Please try again."
        self.assertIn(str.encode(error_msg), response.data)
        ### check that page did not redirected
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action": "/login"})

    
    def test_user_login_invalid_email(self):
        response = self.login('ttester1', 'test.tes@tercom')
        error_msg = "Wrong e-mail address. Please try again."
        self.assertIn(str.encode(error_msg), response.data)
        ### check that page did not redirected
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action" : "/login"})


    def test_manage_profile(self):
        response = self.login('ttester1', 'test@tester.com')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 200)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("h4", text = re.compile('Welcome to Profile Manager'))

    
    def test_edit_profile(self):
        response = self.login('ttester1', 'test@tester.com')
        self.assertEqual(response.status_code, 200)
        user = Hiker.objects.get({'username': 'ttester1'})
        response = self.app.get('/profiles/edit/'+ str(user._id))
        self.assertEqual(response.status_code, 200)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("h4", text = re.compile('Update Profile For: ttester1'))
        response = self.app.post('/profiles/edit/'+ str(user._id), 
                    data = dict(fname = 'Test', lname = 'Tester', origin='Alaska', email='test@tester.com', trails_completed=150, profile_pic='http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg'), 
                    follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        success_msg = "Profile Updated Successfully"
        self.assertIn(str.encode(success_msg), response.data)

        ## have to put this part before logout
    def post_comment(self, body, date_started, hours_taken, minutes_taken, sightings, ratings, trails_id):
        data=dict(body=body, date_started=date_started, hours_taken=hours_taken, minutes_taken=minutes_taken, sightings=sightings, ratings=ratings)
        return self.app.post(
            '/trails/new-comments/'+str(trails_id),
            data=data, #data=dict(body=body, date_started=date_started, hours_taken=hours_taken, minutes_taken=minutes_taken, sightings=sightings, ratings=ratings),
            follow_redirects=True
        )
    
    def test_post_comment(self):
        trails = Trails.objects.get({'trail_name': testTrailName})
        ### html status code 401 if unauthorized to post comment
        response = self.app.get('/trails/new-comments/'+str(trails._id))
        self.assertEqual(response.status_code, 401)

        #if log in success, able to access form to post comments
        response = self.login('ttester1', 'test@tester.com')
        self.assertEqual(response.status_code, 200)
        success_msg = "You logged in successfully as ttester1"
        response = self.app.get('/trails/new-comments/'+str(trails._id))
        self.assertEqual(response.status_code, 200)

        #response = self.post_comment('Testing abc123', "Mar 17, 2019", 2, 20, [dict(tag='tree')], 3, trails._id)
        #print(response.data)
        inner_dict ={'tag':'tree'}
        data = dict(body='Testing abc123', date_started="Mar 17, 2019", hours_taken=2, minutes_taken=20, sightings=json.dumps([inner_dict]),ratings=3)
        response = self.app.post(
            '/trails/new-comments/'+str(trails._id),
            data= data,
            follow_redirects=True
        )
        #print(response.data)

        
        #with app.app_context():
        #    with self.app as c:
        #        form = CommentsForm(**data)
                #form.body.data = 'Testing 123'
                #form.date_started.data = "Mar 17, 2019"
                #form.hours_taken.data = 2
                #form.minutes_taken.data = 20
                #tag = 'tree'
                #form.sightings.data.append(tag.encode())
                #form.ratings.data = 3
                #response = c.post('/trails/new-comments/'+str(trails._id), data=form.data, follow_redirects = True)
                #print(response.data)


#    def test_edit_comment(self):
#        trails = Trails.objects.get({'trail_name': testTrailName})
#        ### html status code 401 if unauthorized to post comment
#        response = self.app.get('/trails/edit-comments/'+str(trails._id))
#        self.assertEqual(response.status_code, 404)

        #if log in success, able to access form to post comments
#        response = self.login('ttester1', 'test@tester.com')
#        self.assertEqual(response.status_code, 200)
#        success_msg = "You logged in successfully as ttester1"
#        response = self.app.get('/trails/edit-comments/'+str(trails._id))
#        self.assertEqual(response.status_code, 200)



    def logout(self):
        return self.app.get('/logout',follow_redirects=True)

    def test_user_logout(self):
        response = self.app.get('/logout')
        success_msg = "You logged out successfully."
        self.assertIn(str.encode(success_msg), response.data)
        ### check that page is redirect back to login page
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action" : "/login"})

    def deregister():
        pass

if __name__ == '__main__':
    unittest.main()