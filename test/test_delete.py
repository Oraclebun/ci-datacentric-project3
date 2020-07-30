import unittest
from bs4 import BeautifulSoup
from models import Hiker
from app import app
import re


class TestDel(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        print("Deleting test object...")

    def login(self, username, email):
        return self.app.post(
            '/login',
            data=dict(username=username, email=email),
            follow_redirects=True
        )

    def test_delete_user(self):
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 200)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("span", text=re.compile(
            'Oops. You need to log in to view this page.'))

        self.login('ttester1', 'test@tester.com')
        user = Hiker.objects.get({'username': 'ttester1'})
        response = self.app.post(
            '/profiles/delete/'+str(user._id), follow_redirects=True)
        success_msg = "Profile Deleted Successfully."
        self.assertIn(str.encode(success_msg), response.data)
