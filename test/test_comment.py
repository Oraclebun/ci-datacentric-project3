import unittest
from models import Hiker, Trails
from app import app
from bs4 import BeautifulSoup
import re

testTrailName = 'The Great Sugar Loaf Trail'


class Test_Comment(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    """
    Test login user can post comment. Post Comment form submit test is
    unable to work for test because of the form structure.
    Need to change form handling in route before posting comments work.
    The same goes for editting comment.
    1. Get test trail by trail name
    2. Get trails/new-comments/trail_id/0. Assert 404
    3. Log in tester
    4. Get trails/edit-comments/trail_id/0. Page redirects back to trails
       page with flash msg.
    5. Get the last editted comment. Assert 200
    6. Post data (edit form). This test fails because of technical problem
       of populating form with app.post data.
    """

    def test_post_comment(self):
        trails = Trails.objects.get({'trail_name': testTrailName})
        # html status code 401 if unauthorized to post comment
        response = self.app.get('/trails/new-comments/'+str(trails._id))
        self.assertEqual(response.status_code, 200)

        self.login('ttester1', 'test@tester.com')
        response = self.app.get('/trails/new-comments/'+str(trails._id))

        # posting the form with the data below does not work for test
        response = self.post_comment('Testing abc123', "Mar 17, 2019", 2, 20, [
                                     'tree', 'birds'], 3, trails._id)

    """
    Test login user is able to edit comment. Edit Comment form submit test is
    unable to work for test because of the form structure.
    Need to change form handling in route before posting comments work.
    1. Get test trail by trail name
    2. Get trails/edit-comments/trail_id/0. Assert 404
    3. Log in tester
    4. Get trails/edit-comments/trail_id/0. Page redirects back to trails page
       with flash msg.
    5. Get the last editted comment. Assert 200
    6. Post data (edit form). This test fails because of technical problem of
       populating form with app.post data.
    """

    def test_edit_comment(self):
        trails = Trails.objects.get({'trail_name': testTrailName})
        self.login('ttester1', 'test@tester.com')

        user = Hiker.objects.get({'username': 'ttester1'})

        ''' get the final comment of the tester'''
        for i, c in enumerate(trails.comments):

            if c.author._id == user._id:
                last_comment = i

        response = self.app.get(
            '/trails/edit-comment/'+str(trails._id)+'/'+str(last_comment))
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("h4", text=re.compile(
            'Edit Comments for '+testTrailName))

        response = self.edit_comment('Testing 123 again', "Apr 18, 2019",
                                     2, 25, ['squirrel', 'birds'], 3,
                                     trails._id, last_comment)
        document = BeautifulSoup(response.data, features='html.parser')
        assert document.find("p", text=re.compile('Another comment to test'))

    """
    Test user delete comment.
    1. User will not be able to delete comment via method = Get
    2. User will not be able to delete other's comments
    3. User should only delete his own comments
    """

    def test_delete_comment(self):
        trails = Trails.objects.get({'trail_name': testTrailName})
        user = Hiker.objects.get({'username': 'ttester1'})
        ''' get the final comment of the tester'''

        self.login('ttester1', 'test@tester.com')

        for i, c in enumerate(trails.comments):
            if c.author._id == user._id:
                last_comment = i

        response = self.app.get(
            '/trails/delete-comment/'+str(trails._id)+'/'+str(last_comment))
        self.assertEqual(response.status_code, 405)

        response = self.app.post(
            '/trails/delete-comment/'+str(trails._id)+'/'+str(last_comment))
        success_msg = "Comment Deleted"
        self.assertIn(str.encode(success_msg), response.data)
