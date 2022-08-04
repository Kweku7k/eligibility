from email.policy import default

from sqlalchemy import null
from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    tempField = db.Column(db.String())
    department = db.Column(db.String(), nullable=True)
    def __repr__(self): 
        return f"Course('{self.id}', '{self.name}','{self.tempField}','{self.department}' )"

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self): 
        return f"Course('{self.id}', '{self.name}', )"

class Electives(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return f"Elective('{self.id}', '{self.name}', )"


class Results(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    number = db.Column(db.String(), nullable=False)
    # Results array
    course = db.Column(db.String(), default="N/A")
    eligibleCourses = db.Column(db.String(), default="N/A")
    availableScienceCourses = db.Column(db.String(), default="N/A")
    otherAvailableCourses = db.Column(db.String(), default="N/A")
    results = db.Column(db.String(), nullable=False)
    passed = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Results('{self.id}', '{self.name}', '{self.passed})"