import unittest
import os
from app import app

app.config['DEBUG'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.testing = True
app.secret_key = os.environ.get("API_SECRET")


if __name__ == '__main__':

    loader = unittest.TestLoader()
    test_reg_suite = loader.discover('test', pattern='test_register.py')
    test_app_suite = loader.discover('test', pattern='test_app.py')
    test_del_suite = loader.discover('test', pattern='test_delete.py')
    '''
    Test Suite to test for:
    1. register profile
    2. get routes for index,directory,top_rated, create_profile and
       trails details page
    '''
    reg_suite = unittest.TestSuite(test_reg_suite)
    '''
    Test Suite to test for:
    1. Registration if username already exists
    2. Registration if user's e-mail is not valid
    3. Login with a valid username and e-mail
    4. Login with an invalid username
    5. Login with an invalid e-mail
    6. Manage user profile access for authenticated user
    7. Edit user profile for authenticated user
    8. Logout user
    '''
    app_suite = unittest.TestSuite(test_app_suite)

    '''
    Test suite to test for delete user profile
    '''
    del_suite = unittest.TestSuite(test_del_suite)

    runner = unittest.TextTestRunner()
    test_result1 = runner.run(reg_suite)
    if test_result1.wasSuccessful():
        test_result2 = runner.run(app_suite)
    if test_result2.wasSuccessful():
        test_result3 = runner.run(del_suite)
