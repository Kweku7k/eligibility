from email import message
from logging import PlaceHolder
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from .models import Course, Electives


grades = ['A1','B2','B3','C4','C5','C6','D7','E8','F9', 'None']
errorMessage = "Please fill this."


class TestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired( message="Please enter a name.") ])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=15, message="Your phone number should be more than 10 digits and less than 15")])
    # course = SelectField('Course', validators=[DataRequired( message="Please enter a name.")], choices=[(cat.name, cat.name) for cat in Course.query.all()] )
    submit = SubmitField('Sign Up')

class Checker(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Phone', validators=[DataRequired(), Length(min=10, max=15, message="Your phone number should be more than 10 digits and less than 15")])
    courseOffered = SelectField('Course', validators=[DataRequired(), NoneOf(['None'],'Please fill this')], choices=[('None',''),('Science', 'Science'), ('Agriculture','Agriculture'), ('Visual Arts','Visual Arts'), ('General Arts', 'General Arts'), ('Business','Business'), ('Home Economics', 'Home Economics')], default=None )
    mathsScore = SelectField('Math',  validators=[DataRequired(), NoneOf(['None'], errorMessage)], default='None', choices=[(grade, grade) for grade in grades])
    englishScore = SelectField('English', validators=[DataRequired(), NoneOf(['None'], errorMessage)], default='None', choices=[(grade, grade) for grade in grades])
    scienceScore = SelectField('Science', validators=[DataRequired(), NoneOf(['None'], errorMessage)], default='None', choices=[(grade, grade) for grade in grades])
    socialScore = SelectField('Social',  validators=[DataRequired(), NoneOf(['None'], errorMessage)], default='None', choices=[(grade, grade) for grade in grades])

    # el1 = SelectField('El1', validators=[DataRequired(), NoneOf(['None'],'Please fill this')], default='None', choices=[(elective.name, elective.name) for elective in Electives.query.all()])
    el1 = SelectField('El1', validators=[DataRequired(), NoneOf(['None'],'Please fill this')], default='None', choices=[('elective.name', 'elective.name')])
    el1grade = SelectField('El1Grade', validators=[DataRequired(), NoneOf(['None'],'Please fill this')], default='None', choices=[(grade, grade) for grade in grades])

    el2 = SelectField('el2', validators=[DataRequired(), NoneOf(['None'],'Please fill this')], default='None', choices=[('elective.name', 'elective.name')])
    el2grade = SelectField('el2grade', validators=[DataRequired(), NoneOf(['None'],'Please fill this')], default='None', choices=[(g,g) for g in grades])

    el3 = SelectField('el3', validators=[DataRequired(), NoneOf(['None'],'Please fill this')], default='None', choices=[('elective.name', 'elective.name')])
    el3grade = SelectField('el3Grade',validators=[DataRequired(), NoneOf(['None'],'Please fill this')], default='None', choices=[(grade, grade) for grade in grades])

    el4 = SelectField('el4', default='None', choices=[('elective.name', 'elective.name')])
    el4grade = SelectField('el4Grade', default='None', choices=[(grade, grade) for grade in grades])


    
    
