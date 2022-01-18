from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    tempField = db.Column(db.String())
    department = db.Column(db.String(), nullable=True)

    # vendor = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    def __repr__(self): 
        return f"Course('{self.id}', '{self.name}', )"

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    # tempField = db.Column(db.String())
    # department = db.Column(db.String(), nullable=True)

    # vendor = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    def __repr__(self): 
        return f"Course('{self.id}', '{self.name}', )"

class Electives(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return f"Elective('{self.id}', '{self.name}', )"