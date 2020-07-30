import unittest
import os
from models import Hiker
from app import app
from bs4 import BeautifulSoup
import re

app.config['DEBUG'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.secret_key = os.environ.get("API_SECRET")


testTrailName = 'The Great Sugar Loaf Trail'


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    def register(self, username, fname, lname, origin, email,
                 trails_completed, profile_pic):
        return self.app.post('/create_profile', data=dict(
            username=username, fname=fname, lname=lname, origin=origin,
            email=email, trails_completed=trails_completed,
            profile_pic=profile_pic), follow_redirects=True)

    """
    Test if user register with an invalid username
    """

    def test_invalid_user_registration_duplicate_username(self):
        response = self.register('ttester1', 'Test', 'Tester', 'Japan',
                                 'different@email.com', 100,
                                 'http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg')
        self.assertEqual(response.status_code, 200)
        error_msg = "User already exists. Please choose another username."
        self.assertIn(str.encode(error_msg), response.data)
        # test form did not submit and page did not redirect
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action": "/create_profile"})

    """
    Test if user register with an invalid e-mail address
    """

    def test_user_registration_invalid_email(self):
        response = self.register('iamtester', 'Test', 'Tester', 'Japan',
                                 'abcde.12345@gemailcom', 0,
                                 'http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg')
        error_msg = "Not a valid e-mail address"
        self.assertIn(str.encode(error_msg), response.data)
        # check form did not submit and page did not redirect
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action": "/create_profile"})

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
        '''
         check that page redirected has a div with
         class=parallax-container(index.html)
        '''
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("div", {"class": "parallax-container"})

    """
    Test user login with an invalid username
    """

    def test_user_login_invalid_username(self):
        response = self.login('ttester2', 'test@tester.com')
        error_msg = "Wrong username. Please try again."
        self.assertIn(str.encode(error_msg), response.data)
        # check that page did not redirected (form did not validate)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action": "/login"})

    """
    Test user login with an invalid e-mail address
    """

    def test_user_login_invalid_email(self):
        response = self.login('ttester1', 'test.tes@tercom')
        error_msg = "Wrong e-mail address. Please try again."
        self.assertIn(str.encode(error_msg), response.data)
        # check that page did not redirected
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action": "/login"})

    """
    Test authenticated user is able to access (manage) user profile
    """

    def test_manage_profile(self):
        response = self.login('ttester1', 'test@tester.com')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 200)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("h4", text=re.compile(
            'Welcome to Profile Manager'))

    """
    Test authenticated user is able to edit user profile
    """

    def test_edit_profile(self):
        response = self.login('ttester1', 'test@tester.com')
        self.assertEqual(response.status_code, 200)
        user = Hiker.objects.get({'username': 'ttester1'})
        response = self.app.get('/profiles/edit/' + str(user._id))
        self.assertEqual(response.status_code, 200)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("h4", text=re.compile(
            'Update Profile For: ttester1'))
        response = self.app.post('/profiles/edit/' + str(user._id),
                                 data=dict(fname='Test', lname='Tester',
                                 origin='Alaska', email='test@tester.com',
                                 trails_completed=150,
                                 profile_pic='http://res.cloudinary.com/c7oud0311/image/upload/v1594909482/project3/profile5_gg2qml.jpg'),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        success_msg = "Profile Updated Successfully"
        self.assertIn(str.encode(success_msg), response.data)

    """
    Test user logout
    """

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_user_logout(self):
        response = self.logout()
        success_msg = "You logged out successfully."
        self.assertIn(str.encode(success_msg), response.data)
        # check that page is redirect back to login page
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("form", {"action": "/login"})


if __name__ == '__main__':
    unittest.main()
