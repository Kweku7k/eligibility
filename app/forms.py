from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from .models import Course


class TestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=15, message="Your phone number should be more than 10 digits and less than 15")])
    course = SelectField('Course', choices=[(cat.name, cat.name) for cat in Course.query.all()] )
    submit = SubmitField('Sign Up')