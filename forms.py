from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, SelectField, DateField, TextAreaField, FieldList, FormField, HiddenField, validators
from wtforms.validators import DataRequired, InputRequired, NumberRange, Email, Length, Optional, ValidationError
from wtforms.fields.html5 import EmailField, IntegerField
from bson.objectid import ObjectId
from models import Hiker

class CreateProfile(FlaskForm):
    username = StringField('Username',validators=[InputRequired()])
    db_user = HiddenField('Username')
    fname = StringField('First Name', validators=[InputRequired()])
    lname = StringField('Last Name', validators=[InputRequired()])
    origin = StringField('Origin', validators=[InputRequired()])
    email = EmailField('E-mail', validators=[InputRequired()])      
    trails_completed = IntegerField('Trails Completed')
    profile_pic = HiddenField("Profile Picture", validators=[InputRequired()])
    submit = SubmitField('Submit')
    def validate_username(self, username):
        user_name = Hiker.objects.get({"username": username.data})
        if user_name != self.db_user.data:
            raise ValidationError("The username already exists.")

class SightingsForm(FlaskForm):
    tag = StringField('e.g. Birds', validators=[Optional()])
    class Meta:
        csrf = False

class CommentsForm(FlaskForm):
    profile = SelectField('Profile', validators=[InputRequired()], coerce=ObjectId)
    body = TextAreaField('Comments', validators=[InputRequired()])
    sightings = FieldList(FormField(SightingsForm, label='e.g. Birds'), label=None, min_entries=1, max_entries=6)
    ratings = RadioField('Ratings', coerce=int, choices = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')])      #, Unique(model= Hiker)])
    date_started = DateField('Date Started Hiking', format='%b %d, %Y')
    hours_taken = IntegerField('Hours Taken')
    minutes_taken = IntegerField('Minutes Taken')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired()])
    email = EmailField('E-mail', validators=[InputRequired()]) 
    submit = SubmitField('Submit')