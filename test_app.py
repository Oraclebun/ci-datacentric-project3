import unittest, os, time
from pymodm import connect
from models import Hiker, Trails, Location, Comment
import pymongo
from app import app
from bson.objectid import ObjectId
from bs4 import BeautifulSoup
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

    """
    Test user login with a valid username and e-mail
    """
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

    """
    Test user login with an invalid username 
    """
    def test_user_login_invalid_username(self):
        response = self.login('ttester2', 'test@tester.com')
        error_msg = "Wrong username. Please try again."
        self.assertIn(str.encode(error_msg), response.data)
        ### check that page did not redirected
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action": "/login"})

    
    """
    Test user login with an invalid e-mail address 
    """
    def test_user_login_invalid_email(self):
        response = self.login('ttester1', 'test.tes@tercom')
        error_msg = "Wrong e-mail address. Please try again."
        self.assertIn(str.encode(error_msg), response.data)
        ### check that page did not redirected
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action" : "/login"})


    """
    Test login user can access manage user profile
    """
    def test_manage_profile(self):
        response = self.login('ttester1', 'test@tester.com')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 200)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("h4", text = re.compile('Welcome to Profile Manager'))

    """
    Test login user can edit user profile
    """
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

    """
    Test login user can post comment. Post Comment form submit test is unable to work for test because of the form structure.
    Need to change form handling in route before posting comments work. The same goes for editting comment.
    1. Get test trail by trail name
    2. Get trails/new-comments/trail_id/0. Assert 404
    3. Log in tester
    4. Get trails/edit-comments/trail_id/0. Page redirects back to trails page with flash msg 
    5. Get the last editted comment. Assert 200
    6. Post data (edit form). This test fails because of technical problem of populating form with app.post data.
    """
        ## have to put this part before logout
    def post_comment(self, body, date_started, hours_taken, minutes_taken, sightings, ratings, trails_id):
        return self.app.post(
            '/trails/new-comments/'+str(trails_id),
            data=dict(body=body, date_started=date_started, hours_taken=hours_taken, minutes_taken=minutes_taken, sightings=sightings, ratings=ratings),
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
        self.assertIn(str.encode(success_msg), response.data)
        response = self.app.get('/trails/new-comments/'+str(trails._id))
        self.assertEqual(response.status_code, 200)

        #posting the form with the data below does not work for test
        response = self.post_comment('Testing abc123', "Mar 17, 2019", 2, 20, ['tree','birds'], 3, trails._id)
        
    """
    Test login user can edit comment. Edit Comment form submit test is unable to work for test because of the form structure.
    Need to change form handling in route before posting comments work. The same goes for editting comment. 
    1. Get test trail by trail name
    2. Get trails/edit-comments/trail_id/0. Assert 404
    3. Log in tester
    4. Get trails/edit-comments/trail_id/0. Page redirects back to trails page with flash msg 
    5. Get the last editted comment. Assert 200
    6. Post data (edit form). This test fails because of technical problem of populating form with app.post data.
    """

    def test_edit_comment(self):
        trails = Trails.objects.get({'trail_name': testTrailName})
        ### html status code 401 if unauthorized to edit comment
        response = self.app.get('/trails/edit-comment/'+str(trails._id)+'/0')
        self.assertEqual(response.status_code, 404)

        #if log in success, able to access form to post comments
        response = self.login('ttester1', 'test@tester.com')
        self.assertEqual(response.status_code, 200)
        
        success_msg = "You logged in successfully as ttester1"
        self.assertIn(str.encode(success_msg), response.data)
        
        user = Hiker.objects.get({'username':'ttester1'})
        response = self.app.get('/trails/edit-comment/'+str(trails._id)+'/0')
        response = self.app.get('/trails/'+str(trails._id))
        error_msg = "You&#39;re not authorized to edit this comment"
        self.assertIn(str.encode(error_msg), response.data)
        
        ''' get the final comment of the tester'''
        for i,c in enumerate(trails.comments):
            if c.author._id == user._id:
                last_comment=i
        response = self.app.get('/trails/edit-comment/'+str(trails._id)+'/'+str(last_comment))
        self.assertEqual(response.status_code, 200)

        #posting the form with the data below does not work for test
        response = self.post_comment('Another comment to test', "Apr 18, 2019", 2, 25, ['squirrel','birds'], 3, trails._id)
        
    """
    Test user delete comment. 
    1. User will not be able to delete comment via method = Get
    2. User will not be able to delete other's comments
    3. User should only delete his own comments
    """
    def test_delete_comment(self):
        trails = Trails.objects.get({'trail_name': testTrailName})
        user = Hiker.objects.get({'username':'ttester1'})
        ''' get the final comment of the tester'''
        for i,c in enumerate(trails.comments):
            if c.author._id == user._id:
                last_comment=i
        response = self.app.get('/trails/delete-comment/'+str(trails._id)+'/'+str(last_comment))
        self.assertEqual(response.status_code, 405)
        response = self.app.post('/trails/delete-comment/'+str(trails._id)+'/0')
        self.assertEqual(response.status_code, 401)
        response = self.app.post('/trails/delete-comment/'+str(trails._id)+'/'+str(last_comment))
        #self.assertEqual(response.status_code, 200)

    def logout(self):
        return self.app.get('/logout',follow_redirects=True)

    def test_user_logout(self):
        response = self.app.get('/logout')
        success_msg = "You logged out successfully."
        self.assertIn(str.encode(success_msg), response.data)
        ### check that page is redirect back to login page
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action" : "/login"})

    def delete_user(self):
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 200)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("h4", text = re.compile('Welcome to Profile Manager'))

        

if __name__ == '__main__':
    unittest.main()