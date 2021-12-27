import re
from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bveqpegotqjcrw:42c1babebbe2323caa9665397a35de15bdf409b3feddbc2de3c81d4b6ef9f994@ec2-44-198-154-255.compute-1.amazonaws.com:5432/d4gc3s7c8o4g7e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
        eligibleCourses.append("Faculty Of Arts and Social Sciences")
        eligibleCourses.append("Faculty Of Law")
        eligibleCourses.append("Central Business School")
    return eligibleCourses

def pharmacy(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade):
    print("Pharmacy Function")
    eligibleCourses = "None"

    ints = [el1, el2, el3, el4]
    grades = [el1grade,el2grade,el3grade,el4grade]

    physics = "F9" 
    biology ="F9"
    chemistry ="F9"
    emaths="F9"
    for idx, val in enumerate(ints):
        print(grades[idx], val)
        if val == 'Physics':
            physics = grades[idx]
            print(physics)
        elif val == 'Biology':
            biology = grades[idx]
        elif val == 'Chemistry':
            chemistry = grades[idx]
        elif val == 'E-Maths':
            emaths = grades[idx]

    # [-1] just takes the last character; so F9 => 9

    if int(chemistry[-1]) <= 4 and int(biology[-1]) <= 4:
        if int(physics[-1]) <=4 or int(emaths[-1]) <=4:
            print("You are eligyle for Pharmacy")
            eligibleCourses = "School of Pharmacy"
        else:
            print("You are a mumu man")
    return eligibleCourses


def civilEngineering(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade):
    print("Pharmacy Function")
    eligibleCourses = "None"

    ints = [el1, el2, el3, el4]
    grades = [el1grade,el2grade,el3grade,el4grade]

    physics = "F9" 
    biology ="F9"
    chemistry ="F9"
    emaths="F9"
    for idx, val in enumerate(ints):
        print(grades[idx], val)
        if val == 'Physics':
            physics = grades[idx]
            print(physics)
        elif val == 'Biology':
            biology = grades[idx]
        elif val == 'Chemistry':
            chemistry = grades[idx]
        elif val == 'E-Maths':
            emaths = grades[idx]

    # [-1] just takes the last character; so F9 => 9

    if int(chemistry[-1]) <= 4 and int(physics[-1]) <= 4:
        if int(biology[-1]) <=4 :
            print("You are eligyle for Civil Engineering")
            eligibleCourses = "Bachelor of Science in Civil Engineering"
        else:
            print("You are a mumu man")
    return eligibleCourses
    

def planning(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade):
    planning = "None"

    groupA = []
    groupB = []

    # Group A
    economics = "F9"
    management = "F9"
    geography = "F9"
    government = "F9"
    mathematics = "F9"
    gka = "F9"

    # Group B
    accounting = "F9"
    technicalDrawing = "F9"
    graphicDesgin = "F9"
    pictureMaking = "F9"
    sculpture = "F9"
    painting = "F9"

    ints = [el1, el2, el3, el4]
    grades = [el1grade,el2grade,el3grade,el4grade]

    for idx, val in enumerate(ints):
        print(grades[idx], val)
        # Group A
        if val == 'Economics':
            # idx is the index, it then looks through the grades array for that item;
            # So if idx = 1;
            # grades[idx] == grades[1]
            # And that gives the grade from the form
            # ie. A1 or B2
            # Then you take the last figure and change it to an integer
            # int(var[-1])
            # Then check if the item is below a 4
            # Thats how you pass.
            economics = grades[idx]
            print("economics")
            print(economics)
            if int(economics[-1]) <= 4:
                groupA.append(economics)
            else:
                print("Failed " + str(idx))
        elif val == 'Management':
            management = grades[idx]
            print("management")
            print(management)
            if int(management[-1]) <= 4:
                groupA.append(management)
            else:
                print("Failed " + str(idx))

        elif val == 'Geography':
            geography = grades[idx]
            print("geography")
            print(geography)
            if int(geography[-1]) <= 4:
                groupA.append(geography)
            else:
                print("Failed " + str(idx))

        elif val == 'Government':
            government = grades[idx]
            print("government")
            print(government)
            if int(government[-1]) <= 4:
                groupA.append(government)
            else:
                print("Failed " + str(idx))

        elif val == 'Mathematics':
            mathematics = grades[idx]
            print("mathematics")
            print(mathematics)
            if int(mathematics[-1]) <= 4:
                groupA.append(mathematics)
            else:
                print("Failed " + str(idx))

        elif val == 'GKA':
            gka = grades[idx]
            print("gka")
            print(gka)
            if int(gka[-1]) <= 4:
                groupA.append(gka)
            else:
                print("Failed " + str(idx))

            # Group B
        elif val == 'Accounting':
            accounting = grades[idx]
            print("Accounting")
            print(accounting)
            if int(accounting[-1]) <= 4:
                groupB.append(accounting)
            else:
                print("Failed " + str(idx))

        elif val == 'Technical Drawing':
            technicalDrawing = grades[idx]
            print("Technical Drawing")
            print(accounting)
            if int(technicalDrawing[-1]) <= 4:
                groupB.append(technicalDrawing)
            else:
                print("Failed " + str(idx))

        elif val == 'Graphic Design':
            graphicDesgin = grades[idx]
            print("Graphic Design")
            print(graphicDesgin)
            if int(graphicDesgin[-1]) <= 4:
                groupB.append(graphicDesgin)
            else:
                print("Failed " + str(idx))

        elif val == 'Picture Making':
            pictureMaking = grades[idx]
            print("Picture Making")
            print(pictureMaking)
            if int(pictureMaking[-1]) <= 4:
                groupB.append(pictureMaking)
            else:
                print("Failed " + str(idx))

        elif val == 'Sculpture':
            sculpture = grades[idx]
            print(sculpture)
            if int(sculpture[-1]) <= 4:
                groupB.append(sculpture)
            else:
                print("Failed " + str(idx))

        elif val == 'Painting':
            painting = grades[idx]
            print(painting)
            if int(painting[-1]) <= 4:
                groupB.append(painting)
            else:
                print("Failed " + str(idx))

        else:
            planning = "You are uneligible for this course"
        

    print("groupB")
    print(groupB)

    print("groupA")
    print(groupA)

    if len(groupA) == 3 or len(groupA) == 2 and len(groupB) == 1:
            planning = "Bachelor of Science in Planning"
    else:
        print("You are a mumu man")


    return planning


def realEstate(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade):
    print("RealEstate Function")
    realestateState = ""
    eligibleCourses = []


    ints = [el1, el2, el3, el4]
    grades = [el1grade,el2grade,el3grade,el4grade]

    economics = "F9" 
    geography ="F9"
    thirdElective ="F9"
    fourthElective="F9"
    fifthElective = "F9"
    # Lol, this is just a loop that takes index, breathe
    for idx, val in enumerate(ints):
        print(grades[idx], val)
        if val == 'Economics':
            economics = grades[idx]
            print("economics")
            print(economics)
        elif val == 'Geography':
            geography = grades[idx]
            print("geography")
            print(geography)
        elif val and thirdElective == "F9":
            thirdElective = grades[idx]
            print("thirdElective")
            print(thirdElective)

        elif val and fourthElective == "F9":
            fourthElective = grades[idx]
            print("fourthElective")
            print(fourthElective)

        elif val == True and fifthElective == "F9":
            fifthElective = grades[idx]
            print("fifthElective")
            print(fifthElective)

        # This might break
        # Check if value is any of these, if not, save val with grade, as el1 ...

    if int(thirdElective[-1]) <= 4 and int(fourthElective[-1]) <= 4:
        print("Passed the first 2 other electives")
        if economics and geography:
            if int(economics[-1]) <=4 and int(geography[-1]) <=4:
                print("You are eligyle for Real Estate")
                realestateState = "Bachelor of Science in Real Estate"
                # eligibleCourses.append('School of Pharmacy')
            else:
                print("You are a mumu man")
        else: 
            if int(geography[-1]) <=4 or int(economics[-1]) <=4:
                print("You are eligible for Real Estate")
                realestateState = "Bachelor of Science in Real Estate"
                print(realestateState)
            else:
                "You are not eligible for Real Estate"
    return realestateState
    

def architecture(el1,el2,el3,el4):
    passed = [] 
    eligibleCourses = "None"

    print("Checking Passed Subjects")
    for i in [el1,el2,el3,el4]:
        if int(i[-1]) <= 4:
            passed.append(i)
            print('Elective ' + i + ' passed')
    print("passed")
    if len(passed) >= 3:
        eligibleCourses= 'Bachelor Of Architecture'
    return eligibleCourses

def computerScience(el1,el2,el3,el4, el1grade, el2grade, el3grade, el4grade):
    print("Computer Science Function")
    eligibleCourses = "None"
    passed = []

    ints = [el1, el2, el3, el4]
    grades = [el1grade,el2grade,el3grade,el4grade]

    physics = False
    # biology ="F9"
    # chemistry ="F9"
    # emaths="F9"
    for idx, val in enumerate(ints):
        print(grades[idx], val)
        if val == 'Physics' and int(grades[idx][-1]) <= 4:
            physics = True
            print(physics)
        elif int(grades[idx][-1]) <= 4:
            passed.append(val)

    # [-1] just takes the last character; so F9 => 9

    print("passed")
    print(passed)
    print(len(passed))

    if physics == True and len(passed) >= 2:
        print("You are eligyle for Computer Science")
        eligibleCourses = "Bachelor Of Science In Computer Science"
        print(eligibleCourses)

    # if int(chemistry[-1]) <= 4 and int(biology[-1]) <= 4:
    #     if int(physics[-1]) <=4 or int(emaths[-1]) <=4:
    #         print("You are eligyle for Pharmacy")
    #         eligibleCourses = "School of Pharmacy"
    #     else:
    #         print("You are a mumu man")
    return eligibleCourses
    

@app.route('/',methods=['GET','POST'])
def home():
    array = []
    els = Electives.query.all()

    array2 = Program.query.all()
    for course in array2:
        array.append(str(course.name))
    
    print("array")
    print(array)
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

# ❤️⚡️
# Function starts here‼️‼️‼️
        if passedCoreSubjects(maths, english, social, science):
            print("Passed The Core Subjects")
            print(creditPass(el1grade, el2grade, el3grade, el4grade))
            yourEligbleCourses = creditPass(el1grade, el2grade, el3grade, el4grade)
            print("Passed For Pharmacy")
            print(pharmacy(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade))
            yourEligbleCourses.append(pharmacy(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade))
            # THIS RETURNS AN ARRAY

        # Returns all the courses from the departments into an array
            print("Array To Be Processed")
            print(yourEligbleCourses)
            for course in yourEligbleCourses:
                courses = Course.query.filter_by(department = course).all()
                for item in courses:
                    passedEls.append(item)

        # We want to find the course by name for the Architecture
            availableCourse = Course.query.filter_by(tempField= realEstate(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first()
            print(availableCourse)
            passedEls.append(availableCourse)

            architectureCourse = Course.query.filter_by(tempField= architecture(el1grade,el2grade,el3grade,el4grade)).first()
            print(architectureCourse)
            passedEls.append(architectureCourse)

            planningCourse = Course.query.filter_by(tempField= planning(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first()
            print(planningCourse)
            passedEls.append(planningCourse)
            
            computerScienceCourse = Course.query.filter_by(tempField= computerScience(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first()
            print("computerScienceCourse")
            passedEls.append(computerScienceCourse)

            print(passedEls)





            # print(Course.query.filter_by(tempField= realEstate(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first())
            # print(realEstate(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade))
            
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
        return render_template('index.html', electives=electives, els=els, grades=grades, array=array)
    return render_template('index.html', electives=electives, els=els, grades=grades, array=array)
    
@app.route("/eligible")
def eligible():
    return render_template('eligible.html',eligibleCourses = eligibleCourses)


@app.route("/courses",methods=['GET','POST'])
def courses(): 

    if request.method=='POST':
        courseName = request.form.get('courseName')
        print(courseName)
        newCourse = Course(tempField=courseName,name=courseName, department= request.form.get('department'))
        db.session.add(newCourse)
        db.session.commit()
        return redirect('')
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)


@app.route("/electives",methods=['GET','POST'])
def electives(): 
    if request.method=='POST':
        electiveName = request.form.get('electiveName')
        print(electiveName)
        newElective = Electives(name=electiveName)
        db.session.add(newElective)
        db.session.commit()
        return redirect('')
    electives = Electives.query.all()
    return render_template('electives.html', electives=electives)


@app.route("/programs",methods=['GET','POST'])
def programs(): 

    if request.method=='POST':
        programName = request.form.get('program')
        print(programName)
        print("programName")
        newProgram = Program(name=programName)
        db.session.add(newProgram)
        db.session.commit()
        return redirect('')
    programs = Program.query.all()
    return render_template('program.html', programs=programs)


@app.route("/delete/<int:id>")
def delete(id):
    course = Course.query.filter_by(id = id).first()
    print(course)
    db.session.delete(course)
    db.session.commit()
    # return redirect('courses')
    return redirect(url_for('courses'))


@app.route("/deleteElective/<int:id>")
def deleteElective(id):
    elective = Electives.query.filter_by(id = id).first()
    print(elective)
    db.session.delete(elective)
    db.session.commit()
    # return redirect('courses')
    return redirect(url_for('electives'))
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)

    