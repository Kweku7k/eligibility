from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(), nullable=True)
    # vendor = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    def __repr__(self): 
        return f"Course('{self.id}', '{self.name}', )"

@app.route('/',methods=['GET','POST'])
def home():
    electives = Course.query.all()
    grades = ['A1','B2','B3','C4','C5','C6','D7','E8','F9']


    if request.method=='POST':
        print('request.form')
        maths = request.form.get('maths')
        english = request.form.get('english')
        social = request.form.get('social')
        science = request.form.get('science')
        el1 = request.form.get('el1')
        el1grade = request.form.get('el1grade')
        el2 = request.form.get('el2')
        el2grade = request.form.get('el2grade')
        el3 = request.form.get('el3')
        el3grade = request.form.get('el3grade')
        el4 = request.form.get('el4')
        el4grade = request.form.get('el4grade')

        print("Maths = " + maths)
        print("english = " + english)
        print("social = " + social)
        print("science = " + science)
        print(str(el1) + " = " + str(el1grade))
        print(str(el2) + " = " + str(el2grade))
        print(str(el3) + " = " + str(el3grade))
        print(str(el4) + " = " + str(el4grade))
     
        return redirect(url_for('eligible'))

    if request.method == 'GET':
        return render_template('index.html', electives=electives, grades=grades)


    return render_template('index.html', electives=electives, grades=grades)

@app.route("/eligible",methods=['GET','POST'])
def eligible():
    return render_template('eligible.html')


@app.route("/courses",methods=['GET','POST'])
def courses(): 

    if request.method=='POST':
        courseName = request.form.get('courseName')
        print(courseName)
        newCourse = Course(name=courseName)
        db.session.add(newCourse)
        db.session.commit()
        return redirect('')
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
