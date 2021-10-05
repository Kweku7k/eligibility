from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bveqpegotqjcrw:42c1babebbe2323caa9665397a35de15bdf409b3feddbc2de3c81d4b6ef9f994@ec2-44-198-154-255.compute-1.amazonaws.com:5432/d4gc3s7c8o4g7e'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    department = db.Column(db.String(), nullable=True)
    # vendor = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    def __repr__(self): 
        return f"Course('{self.id}', '{self.name}', )"


# eligibleCourses = []
ineligible = False
def passedCoreSubjects(core1,core2,core3,core4):
    corePass = []
    passedAtLeast3 = False;


    print("Checking Core Subjects")
    for i in [core1,core2,core3,core4]:
        if int(i[-1]) <= 4:
            corePass.append(i)
            print('Core ' + i + ' passed')
    print("passed ALL CORE")
    if len(corePass) >= 3:
        passedAtLeast3 = True;

    print("Passed3" + str(passedAtLeast3))
    return passedAtLeast3

def creditPass(el1,el2,el3,el4):
    passed = [] 
    eligibleCourses = []

    print("Checking Passed Subjects")
    for i in [el1,el2,el3,el4]:
        if int(i[-1]) <= 4:
            passed.append(i)
            print('Elective ' + i + ' passed')
    print("passed")
    if len(passed) >= 3:
        eligibleCourses.append("Faculty of Arts and Social Sciences")
        eligibleCourses.append("Faculty Of Law")
        eligibleCourses.append("Central Business School")
    return eligibleCourses

@app.route('/',methods=['GET','POST'])
def home():
    ineligible=False
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

        yourEligbleCourses = []

        passedEls = []

        if passedCoreSubjects(maths, english, social, science):
            print("Passed The Core Subjects")
            print(creditPass(el1grade, el2grade, el3grade, el4grade))
            yourEligbleCourses = creditPass(el1grade, el2grade, el3grade, el4grade)

            for course in yourEligbleCourses:
                passedEls.append(Course.query.filter_by(department = course).all())
            
        # eligibleCourses = []
        print("yourEligbleCourses")
        print(yourEligbleCourses) 
        # print(yourEligbleCourses)
        if yourEligbleCourses:
            print(yourEligbleCourses)
        else:
            ineligible = True

        print("passed")
        # return redirect(url_for('eligible'))
        return render_template('eligible.html',eligibleCourses = passedEls, ineligible=ineligible)
        # return redirect('')

    if request.method == 'GET':
        eligibleCourses = []
        print(eligibleCourses)
        return render_template('index.html', electives=electives, grades=grades)
    return render_template('index.html', electives=electives, grades=grades)

@app.route("/eligible")
def eligible():
    return render_template('eligible.html',eligibleCourses = eligibleCourses)


@app.route("/courses",methods=['GET','POST'])
def courses(): 

    if request.method=='POST':
        courseName = request.form.get('courseName')
        print(courseName)
        newCourse = Course(name=courseName, department= request.form.get('department'))
        db.session.add(newCourse)
        db.session.commit()
        return redirect('')
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)


@app.route("/delete/<int:id>")
def delete(id):
    course = Course.query.filter_by(id = id).first()
    print(course)
    db.session.delete(course)
    db.session.commit()
    # return redirect('courses')
    return redirect(url_for('courses'))
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)

    