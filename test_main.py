import unittest
import os
from models import Hiker, Trails, Location, Comment
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


if __name__ == '__main__':

    loader = unittest.TestLoader()
    test_reg_suite = loader.discover('.', pattern='test_register.py')
    test_app_suite = loader.discover('.', pattern='test_app.py')
    reg_suite = unittest.TestSuite(test_reg_suite)
    app_suite = unittest.TestSuite(test_app_suite)
    runner = unittest.TextTestRunner()
    #test_result1 = runner.run(reg_suite)
    #if test_result1.wasSuccessful():
    test_result2 = runner.run(app_suite)
