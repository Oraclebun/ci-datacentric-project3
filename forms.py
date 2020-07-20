from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, SelectField, DateField, TextAreaField, FieldList, FormField, HiddenField, validators
from wtforms.validators import DataRequired, InputRequired, NumberRange, Length, Optional, ValidationError
from wtforms.fields.html5 import EmailField, IntegerField
from bson.objectid import ObjectId
from models import Hiker
import re


class CreateProfile(FlaskForm):
    username = StringField('Username',validators=[InputRequired(), Length(min=5, max=20, message="Username have to be 5-20 Chars")])
    fname = StringField('First Name', validators=[InputRequired(), Length(min=2, max=20, message="First Name have to be 2-30 Chars")])
    lname = StringField('Last Name', validators=[InputRequired(), Length(min=2, max=20, message="Last Name have to be 2-20 Chars")])
    origin = StringField('Origin', validators=[InputRequired()])
    email = EmailField('E-mail', validators=[InputRequired()])
    trails_completed = IntegerField('Trails Completed')
    profile_pic = HiddenField("Profile Picture", validators=[InputRequired(message="Profile Picture is required.")])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        try:
            message = 'User already exists. Please choose another username.'
            db_user = Hiker.objects.get({"username": username.data})
            if db_user:
                raise ValidationError(message)    
        except Hiker.DoesNotExist:
            pass

    def validate_email(self,email):
            message = 'Not a valid e-mail address'
            EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')
            if not EMAIL_REGEX.match(email.data):
                raise ValidationError(message)


class UpdateProfile(FlaskForm):
    fname = StringField('First Name', validators=[InputRequired(), Length(min=2, max=20, message="First Name have to be 2-30 Chars")])
    lname = StringField('Last Name', validators=[InputRequired(), Length(min=2, max=20, message="Last Name have to be 2-20 Chars")])
    origin = StringField('Origin', validators=[InputRequired()])
    email = EmailField('E-mail', validators=[InputRequired()])     
    trails_completed = IntegerField('Trails Completed', validators=[InputRequired()])
    profile_pic = HiddenField("Profile Picture", validators=[Optional()])
    submit = SubmitField('Submit')
        
    def validate_email(self,email):
        message = 'Not a valid e-mail address'
        EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')
        if not EMAIL_REGEX.match(email.data):
            raise ValidationError(message)


class SightingsForm(FlaskForm):
    tag = StringField('e.g. Birds', validators=[Optional()])


    class Meta:
        csrf = False


class CommentsForm(FlaskForm):
    body = TextAreaField('Comments', validators=[InputRequired()])
    sightings = FieldList(FormField(SightingsForm, label='e.g. Birds'), label=None, min_entries=1, max_entries=6)
    ratings = RadioField('Ratings', coerce=int, choices = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')])      #, Unique(model= Hiker)])
    date_started = DateField('Date Started Hiking', format='%b %d, %Y')
    hours_taken = IntegerField('Hours Taken', validators=[NumberRange(min=0, max=23, message="Number of hours cannot exceed 23")])
    minutes_taken = IntegerField('Minutes Taken',validators=[NumberRange(min=0, max=59, message="Number of minutes cannot exceed 59")])
    submit = SubmitField('Submit')
