import json
import pprint
from sqlalchemy import true
from app import app
from app.models import *
from flask import jsonify, redirect,url_for,render_template,request,flash, session
from .forms import TestForm, Checker
import urllib.request, urllib.parse
import urllib

# eligibleCourses = []  
passFigure = 6
ineligible = False

def convertToIds(courses):
    courseIds = []
    print(courses)
    for course in courses:
        if course != None:
            print(course)
            print(course.id)
            courseIds.append(course.id)
    return courseIds

def passedCoreSubjects(core1,core2,core3,core4):
    corePass = []
    passedAtLeast3 = False

    print("Checking Core Subjects")
    # [-1] -> This takes the last character from the string
    for i in [core1,core2,core3,core4]:
        if int(i[-1]) <= passFigure:
            corePass.append(i)
            print('Core ' + i + ' passed')
    print("passed ALL CORE")
    if len(corePass) >= 3:
        passedAtLeast3 = True
        print("Passed 3 cored")

    print("Passed3" + str(passedAtLeast3))
    return passedAtLeast3

def creditPass(el1,el2,el3,el4):
    passed = [] 
    eligibleCourses = []

    print("Checking Passed Subjects")
    for i in [el1,el2,el3,el4]:
        print("i")
        print(i)
        print(len(i))
        print(type(i))
        if int(i[-1]) <= passFigure:
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

    if int(chemistry[-1]) <= passFigure and int(biology[-1]) <= passFigure:
        if int(physics[-1]) <=passFigure or int(emaths[-1]) <=passFigure:
            print("You are eligyle for Pharmacy")
            eligibleCourses = "School of Pharmacy"
        else:
            print("You are a mumu man")
    return eligibleCourses


def civilEngineering(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade):
    print("Civil Engineering Function")
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

    if int(chemistry[-1]) <= passFigure and int(emaths[-1]) <= passFigure:
        if int(physics[-1]) <=passFigure or int(biology[-1]) <=passFigure:
            print("You are eligble for Civil Engineering")
            eligibleCourses = "Bachelor Of Science In Civil Engineering"
        else:
            print("Failed Civil Engineering")
    return eligibleCourses


def physicianAssistant(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade):
    print("Physician Assistant Function")
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

    if int(chemistry[-1]) <= passFigure and int(biology[-1]) <= passFigure and int(physics[-1]) <=passFigure :
        # if int(physics[-1]) <=passFigure or int(biology[-1]) <=passFigure:
            print("You are eligble for Physician Assistant")
            eligibleCourses = "Bachelor Of Science In Physician Assisstanship"
    else:
            print("Failed Physiciain Assistantship")
    print("Inside the pa function, final output is " + eligibleCourses)
    return eligibleCourses

# def computerScience(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade):
#     print("Computer Function")
#     eligibleCourses = "None"

#     ints = [el1, el2, el3, el4]
#     grades = [el1grade,el2grade,el3grade,el4grade]

#     physics = "F9" 
#     biology ="F9"
#     chemistry ="F9"
#     emaths="F9"
#     for idx, val in enumerate(ints):
#         print(grades[idx], val)
#         if val == 'Physics':
#             physics = grades[idx]
#             print(physics)
#         elif val == 'Biology':
#             biology = grades[idx]
#         elif val == 'Chemistry':
#             chemistry = grades[idx]
#         elif val == 'E-Maths':
#             emaths = grades[idx]

#     # [-1] just takes the last character; so F9 => 9

#     if int(chemistry[-1]) <= passFigure and int(biology[-1]) <= passFigure:
#         if int(physics[-1]) <=passFigure or int(emaths[-1]) <=passFigure:
#             print("You are eligyle for Pharmacy")
#             eligibleCourses = "School of Pharmacy"
#         else:
#             print("You are a mumu man")
#     return eligibleCourses


# def civilEngineering(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade):
#     print("Pharmacy Function")
#     eligibleCourses = "None"

#     ints = [el1, el2, el3, el4]
#     grades = [el1grade,el2grade,el3grade,el4grade]

#     physics = "F9" 
#     biology ="F9"
#     chemistry ="F9"
#     emaths="F9"
#     for idx, val in enumerate(ints):
#         print(grades[idx], val)
#         if val == 'Physics':
#             physics = grades[idx]
#             print(physics)
#         elif val == 'Biology':
#             biology = grades[idx]
#         elif val == 'Chemistry':
#             chemistry = grades[idx]
#         elif val == 'E-Maths':
#             emaths = grades[idx]

#     # [-1] just takes the last character; so F9 => 9

#     if int(chemistry[-1]) <= passFigure and int(physics[-1]) <= passFigure:
#         if int(biology[-1]) <=passFigure :
#             print("You are eligyle for Civil Engineering")
#             eligibleCourses = "Bachelor of Science in Civil Engineering"
#         else:
#             print("You are a mumu man")
#     return eligibleCourses
    

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
            if int(economics[-1]) <= passFigure:
                groupA.append(economics)
            else:
                print("Failed " + str(idx))
        elif val == 'Management':
            management = grades[idx]
            print("management")
            print(management)
            if int(management[-1]) <= passFigure:
                groupA.append(management)
            else:
                print("Failed " + str(idx))

        elif val == 'Geography':
            geography = grades[idx]
            print("geography")
            print(geography)
            if int(geography[-1]) <= passFigure:
                groupA.append(geography)
            else:
                print("Failed " + str(idx))

        elif val == 'Government':
            government = grades[idx]
            print("government")
            print(government)
            if int(government[-1]) <= passFigure:
                groupA.append(government)
            else:
                print("Failed " + str(idx))

        elif val == 'Mathematics':
            mathematics = grades[idx]
            print("mathematics")
            print(mathematics)
            if int(mathematics[-1]) <= passFigure:
                groupA.append(mathematics)
            else:
                print("Failed " + str(idx))

        elif val == 'GKA':
            gka = grades[idx]
            print("gka")
            print(gka)
            if int(gka[-1]) <= passFigure:
                groupA.append(gka)
            else:
                print("Failed " + str(idx))

            # Group B
        elif val == 'Accounting':
            accounting = grades[idx]
            print("Accounting")
            print(accounting)
            if int(accounting[-1]) <= passFigure:
                groupB.append(accounting)
            else:
                print("Failed " + str(idx))

        elif val == 'Technical Drawing':
            technicalDrawing = grades[idx]
            print("Technical Drawing")
            print(accounting)
            if int(technicalDrawing[-1]) <= passFigure:
                groupB.append(technicalDrawing)
            else:
                print("Failed " + str(idx))

        elif val == 'Graphic Design':
            graphicDesgin = grades[idx]
            print("Graphic Design")
            print(graphicDesgin)
            if int(graphicDesgin[-1]) <= passFigure:
                groupB.append(graphicDesgin)
            else:
                print("Failed " + str(idx))

        elif val == 'Picture Making':
            pictureMaking = grades[idx]
            print("Picture Making")
            print(pictureMaking)
            if int(pictureMaking[-1]) <= passFigure:
                groupB.append(pictureMaking)
            else:
                print("Failed " + str(idx))

        elif val == 'Sculpture':
            sculpture = grades[idx]
            print(sculpture)
            if int(sculpture[-1]) <= passFigure:
                groupB.append(sculpture)
            else:
                print("Failed " + str(idx))

        elif val == 'Painting':
            painting = grades[idx]
            print(painting)
            if int(painting[-1]) <= passFigure:
                groupB.append(painting)
            else:
                print("Failed " + str(idx))

        else:
            planning = "You are uneligible for this course"
        

    print("groupB")
    print(groupB)

    print("groupA")
    print(groupA)

    if len(groupA) >= 3 or len(groupA) == 2 and len(groupB) == 1:
            # planning = "Bachelor Of Science In Planning"
        print("TXY - Bachelor Of Science In Planning")
        planning = "Bachelor Of Science In Planning"
    else:
        print("You are a mumu man")


    return planning

# -------------

def nursing(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade):
    print("Nursing Function")
    nursing = ""

    groupA = []
    groupB = []

    # General Arts
    geography = "F9"
    government = "F9"
    gka = "F9"
    literature = "F9"
    french = "F9"
    history = "F9"
    crs = "F9"
    emaths = "F9"

    # Science
    biology = "F9"
    chemistry = "F9"
    physics = "F9"

    # Agric Science
    agriculture = "F9"

    # Home Econs
    MIL = "F9"
    economics = "F9"
    foodNnutrition = "F9"
    textiles = "F9"
    french = "F9"

   

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
            if int(economics[-1]) <= passFigure:
                groupA.append(economics)
            else:
                print("Failed " + str(idx))
        elif val == 'Geography':
            geography = grades[idx]
            print("geography")
            print(geography)
            if int(geography[-1]) <= passFigure:
                groupA.append(geography)
                print("Passed " + val)
            else:
                print("Failed " + str(idx))

        elif val == 'Goverment':
            government = grades[idx]
            print(government)
            if int(government[-1]) <= passFigure:
                groupA.append(government)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))
        elif val == 'GKA':
            gka = grades[idx]
            print(gka)
            if int(gka[-1]) <= passFigure:
                groupA.append(gka)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))

        elif val == 'Literature':
            literature = grades[idx]
            print(literature)
            if int(literature[-1]) <= passFigure:
                groupA.append(literature)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))

        elif val == 'French':
            french = grades[idx]
            print(french)
            if int(french[-1]) <= passFigure:
                groupA.append(french)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))

        elif val == 'History':
            history = grades[idx]
            print(history)
            if int(history[-1]) <= passFigure:
                groupA.append(history)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))

        elif val == 'CRS':
            crs = grades[idx]
            print(crs)
            if int(crs[-1]) <= passFigure:
                groupA.append(crs)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))
        elif val == 'E-Maths':
            emaths = grades[idx]
            print(emaths)
            if int(emaths[-1]) <= passFigure:
                groupA.append(emaths)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))
                # Science Courses
        elif val == 'Chemistry':
            chemistry = grades[idx]
            print(chemistry)
            if int(chemistry[-1]) <= passFigure:
                groupA.append(chemistry)
                print("Passed " + val)
            else:
                print("Failed " + str(idx))
        elif val == 'Biology':
            biology = grades[idx]
            print(biology)
            if int(biology[-1]) <= passFigure:
                groupA.append(biology)
                print("Passed " + val)
            else:
                print("Failed " + str(idx))
        elif val == 'Physics':
            physics = grades[idx]
            print(physics)
            if int(physics[-1]) <= passFigure:
                groupA.append(physics)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))
        elif val == 'Agriculture':
            agriculture = grades[idx]
            print(agriculture)
            if int(agriculture[-1]) <= passFigure:
                groupA.append(agriculture)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))
        elif val == 'MIL':
            MIL = grades[idx]
            print(MIL)
            if int(MIL[-1]) <= passFigure:
                groupA.append(MIL)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))
        elif val == 'Food And Nutrition':
            foodNnutrition = grades[idx]
            print(foodNnutrition)
            if int(foodNnutrition[-1]) <= passFigure:
                groupA.append(foodNnutrition)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))
        elif val == 'textiles':
            textiles = grades[idx]
            print(textiles)
            if int(textiles[-1]) <= passFigure:
                groupA.append(textiles)
                print("Passed " + val)

            else:
                print("Failed " + str(idx))

        else:
            nursing = "You are uneligible for this course"
        

    print("groupB")
    print(groupB)

    print("groupA")
    print(groupA)

    # if len(groupA) == 3 or len(groupA) == 2 and len(groupB) == 1:
    if len(groupA) >= 3:
        # nursing = Course.query.filter_by("Bachelor of Science in Nursing").first()
        nursing = "Bachelor Of Science In Nursing"
        print(nursing)
    else:
        print("You are a mumu man")

    print(nursing)
    print("Lin3 608")


    return nursing
# -------------




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

    if int(thirdElective[-1]) <= passFigure and int(fourthElective[-1]) <= passFigure:
        print("Passed the first 2 other electives")
        if economics and geography:
            if int(economics[-1]) <=passFigure and int(geography[-1]) <=passFigure:
                print("You are eligible for Real Estate")
                realestateState = "Bachelor Of Science In Real Estate"
                # eligibleCourses.append('School of Pharmacy')
            else:
                print("You are a mumu man")
        else: 
            if int(geography[-1]) <=passFigure or int(economics[-1]) <=passFigure:
                print("You are eligible for Real Estate")
                realestateState = "Bachelor Of Science In Real Estate"
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
        print("You are eligible for Architecture")
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
        if val == 'Physics' and int(grades[idx][-1]) <= passFigure:
            physics = True
            print(physics)
        elif int(grades[idx][-1]) <= passFigure:
            passed.append(val)

    # [-1] just takes the last character; so F9 => 9

    print("passed")
    print(passed)
    print(len(passed))

    if physics == True and len(passed) >= 2:
        print("You are eligible for Computer Science")
        eligibleCourses = "Bachelor Of Science In Computer Science"
        print(eligibleCourses)

    # if int(chemistry[-1]) <= 4 and int(biology[-1]) <= 4:
    #     if int(physics[-1]) <=4 or int(emaths[-1]) <=4:
    #         print("You are eligyle for Pharmacy")
    #         eligibleCourses = "School of Pharmacy"
    #     else:
    #         print("You are a mumu man")
    return eligibleCourses

def technology(el1,el2,el3,el4, el1grade, el2grade, el3grade, el4grade):
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
        if val == 'Physics' and int(grades[idx][-1]) <= passFigure:
            physics = True
            print(physics)
        elif int(grades[idx][-1]) <= passFigure:
            passed.append(val)

    # [-1] just takes the last character; so F9 => 9

    print("passed")
    print(passed)
    print(len(passed))

    if physics == True and len(passed) >= 2:
        print("You are eligible for Computer Science")
        eligibleCourses = "School of Engeneering and Technology"
        print(eligibleCourses)

    # if int(chemistry[-1]) <= 4 and int(biology[-1]) <= 4:
    #     if int(physics[-1]) <=4 or int(emaths[-1]) <=4:
    #         print("You are eligyle for Pharmacy")
    #         eligibleCourses = "School of Pharmacy"
    #     else:
    #         print("You are a mumu man")
    return eligibleCourses
    
@app.route('/test')
def method_name():
    pass
    form = TestForm()
    return render_template('test.html', form=form)



@app.route('/',methods=['GET','POST'])
def home():

    # if request.is_json:
    #     return jsonify({'message':"Wrong Body Try Again."}),500
    form = Checker()

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

    if request.method == 'POST':
        print("POST REQUEST")

        if request.is_json:
            body = request.json

            print('JSON BODY')
            print(body)
            pprint.pprint(body)

            name = body.get('name','None')
            number = body.get('number','None')
            maths = body.get('mathsScore','None')
            english = body.get('englishScore','None')
            social = body.get('socialScore','None')
            science = body.get('scienceScore','None')
            # --------------------------------
            el1 = body.get('el1','None')
            el1grade = body.get('el1grade','None')
            # --------------------------------
            el2 = body.get('el2','None')
            el2grade = body.get('el2grade','None')
            # --------------------------------
            el3 = body.get('el3','None')
            el3grade = body.get('el3grade','None')
            # --------------------------------
            el4 = body.get('el4','None')
            el4grade = body.get('el4grade','None')

            courseOffered = body.get('courseOffered', 'None')

            
            pprint.pprint(body)

        else:

            name = form.name.data
            number = form.number.data
            maths = form.mathsScore.data
            english = form.englishScore.data
            social = form.socialScore.data
            science = form.scienceScore.data
            # --------------------------------
            el1 = form.el1.data
            el1grade = form.el1grade.data
            # --------------------------------
            el2 = form.el2.data
            el2grade = form.el2grade.data
            # --------------------------------
            el3 = form.el3.data
            el3grade = form.el3grade.data
            # --------------------------------
            el4 = form.el4.data
            print("EL4 FORM DATA")

            if form.el4grade.data == 'None' or form.el4grade.data == None:
                el4grade = 'F9'
            else:
                el4grade = form.el4grade.data

            courseOffered = form.courseOffered.data
            

        if form.validate_on_submit() or request.is_json:
            # print("Forms validated successfully")
            electivesArray = []

            # print('name')
            # print('request.form')

            # name = form.name.data
            # number = form.number.data
            # maths = form.mathsScore.data
            # english = form.englishScore.data
            # social = form.socialScore.data
            # science = form.scienceScore.data
            # # --------------------------------
            # el1 = form.el1.data
            # el1grade = form.el1grade.data
            # # --------------------------------
            # el2 = form.el2.data
            # el2grade = form.el2grade.data
            # # --------------------------------
            # el3 = form.el3.data
            # el3grade = form.el3grade.data
            # # --------------------------------
            # el4 = form.el4.data
            # print("EL4 FORM DATA")
            # if form.el4grade.data == 'None' or form.el4grade.data == None:
            #     el4grade = 'F9'
            # else:
            #     el4grade = form.el4grade.data
            # --------------------------------
            electivesArray.append(el1)
            electivesArray.append(el2)
            electivesArray.append(el3)
            electivesArray.append(el4)
            print("Printing electives array")
            print(electivesArray)

            electives_array = set(electivesArray)
            contains_duplicates = len(electives_array) != len(electivesArray)
            print(contains_duplicates)
            

                
            sendtelegram(
            "Name = " + name + '\n'+ 
            "Course = " + courseOffered + '\n'+ 
            "Number = " + number + '\n'+ 
            "Maths = " + maths + '\n' + 
            "English = " + english + '\n' + 
            "Social Studies = " + social + '\n' + 
            "Science = " + science + '\n' + 
            str(el1) + " = " + str(el1grade) + '\n' + 
            str(el2) + " = " + str(el2grade) + '\n' +
            str(el3) + " = " + str(el3grade) + '\n' +
            str(el4) + " = " + str(el4grade) + '\n' 
        )   


            if contains_duplicates:
                print("No Please, contains duplicates")
                flash("Duplication is not allowed ","info")
                sendtelegram("There was an error")
                return redirect(request.referrer)
            elif len(number) != 10:
                print(number)
                flash("Problem with personal information ","info")
                return redirect(request.referrer)
            else:
                session.clear()



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
                print("Check For Pharmacy")
                print(pharmacy(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade))
                yourEligbleCourses.append(pharmacy(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade))
                # yourEligbleCourses.append(technology(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade))

                # THIS RETURNS AN ARRAY

            # Returns all the courses from the departments into an array
                print("Array To Be Processed")
                print(yourEligbleCourses)
                for course in yourEligbleCourses:
                    courses = Course.query.filter_by(department = course).all()
                    print("Initial Out Put to PassedEls")
                    for item in courses:
                        passedEls.append(item)
                        print(item)

            # We want to find the course by name for the Architecture
                availableCourse = Course.query.filter_by(tempField= realEstate(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first()
                print(availableCourse)
                passedEls.append(availableCourse)

                architectureCourse = Course.query.filter_by(tempField= architecture(el1grade,el2grade,el3grade,el4grade)).first()
                print("architectureCourse")
                print(architectureCourse)
                passedEls.append(architectureCourse)

                planningCourse = Course.query.filter_by(tempField= planning(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first()
                print("planningCourse")
                print(planningCourse)
                passedEls.append(planningCourse)

                nursingCourse = Course.query.filter_by(tempField= nursing(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first()
                print("nursingCourse")
                print(nursingCourse)
                passedEls.append(nursingCourse)
                
                computerScienceCourse = Course.query.filter_by(tempField= computerScience(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first()
                print(computerScienceCourse)
                passedEls.append(computerScienceCourse)
                if computerScienceCourse:
                    passedEls.append(Course.query.filter_by(tempField= "Bachelor Of Science In Information Technology").first())

                PhysicianAssistantCourse = Course.query.filter_by(tempField= physicianAssistant(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first()
                print(PhysicianAssistantCourse)
                passedEls.append(PhysicianAssistantCourse)
                print("Just passed Physician Assistanship")
                if PhysicianAssistantCourse:
                    print('Adding Public Health to passedEls')
                    pHealth = Course.query.filter_by(tempField="Bachelor Of Science In Public Health").first()
                    
                    print(pHealth)
                    passedEls.append(pHealth)
                print(passedEls)

                civilEngineeringCourse = Course.query.filter_by(tempField= civilEngineering(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first()
                print (civilEngineeringCourse)
                passedEls.append(civilEngineeringCourse)

                # print(Course.query.filter_by(tempField= realEstate(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade)).first())
                # print(realEstate(el1,el2,el3,el4,el1grade,el2grade,el3grade,el4grade))

            # eligibleCourses = []

            print("passedEls")
            # print(passedEls)

            availableScienceCourses = []
            otherAvailableCourses = []
            availableBusinessCourses = []

            # courseOffered = form.courseOffered.data

            allEligibleCourses = []

            print("courses!")
            for course in passedEls:
                if course != None and course.department == "School of Pharmacy" or course != None and course.department == "School of Medicine and Health Sciences" or course != None and course.department == "School of Engeneering and Technology":
                    print(course)
                    availableScienceCourses.append(course)
                elif course != None and course.department == "Central Business School":
                    print(course)
                    availableBusinessCourses.append(course)  
                else:
                    otherAvailableCourses.append(course)


            # Interms of order

            if courseOffered == 'Science':
                for course in availableScienceCourses:
                    allEligibleCourses.append(course)
                for course in availableBusinessCourses:
                    allEligibleCourses.append(course)
                for course in otherAvailableCourses:
                    allEligibleCourses.append(course)
            elif courseOffered == 'Business':
                for course in availableBusinessCourses:
                    allEligibleCourses.append(course)
                for course in availableScienceCourses:
                    allEligibleCourses.append(course)
                for course in otherAvailableCourses:
                    allEligibleCourses.append(course)
            else:
                allEligibleCourses = passedEls
                    

            # Add New Result to Database
            print('Name---------------------')
            print(name)
            print('Number---------------------')
            print(number)
            print('courseOffered---------------------')
            print(courseOffered)
            print('eligibleCourses---------------------')
            # print(str(eligibleCourses))
            print('allEligibleCourses---------------------')
            print(allEligibleCourses)
            print('available Courses ---------------------')
            print(availableCourse)
            print('otherAvailableCourses---------------------')
            print(otherAvailableCourses)
            print('ineligble---------------------')
            print(ineligible)

            if ineligible :
                passedEligibleTest = False
            else:
                passedEligibleTest = True
                
            # This returns an array of all the courses
            # Conversion to an array of id's
            print("Before return")
            print(type(allEligibleCourses))

            allEligibleCourseIds = convertToIds(allEligibleCourses)
            print(otherAvailableCourses)
            

            newResult = Results(name=name, number=number, course=courseOffered, results=str(allEligibleCourseIds), eligibleCourses=json.dumps(allEligibleCourseIds), availableScienceCourses=str(availableScienceCourses), otherAvailableCourses=str(otherAvailableCourses), passed=passedEligibleTest )
            db.session.add(newResult)
            db.session.commit()

            print("yourEligbleCourses")
            print(yourEligbleCourses) 
            # print(yourEligbleCourses)
            if yourEligbleCourses == [] or yourEligbleCourses != ['None']:
                print(yourEligbleCourses)
            else:
                ineligible = True

            print("passed")
            print("availableScienceCourses")
            print(availableScienceCourses)
            sendtelegram(str(availableScienceCourses))
            # return redirect(url_for('eligible'))
        
            

            session.clear()


            response = {
                "name":name,
                "eligibleCourses":convertCourseToString(allEligibleCourses),
                "availableScienceCourses":convertCourseToString(availableScienceCourses),
                "otherAvailableCourses":convertCourseToString(otherAvailableCourses),
                "otherAvailableCourses":convertCourseToString(otherAvailableCourses),
                "ineligible":ineligible
            }

            if request.is_json:
                pprint.pprint(response)
                return response
            else:
                return render_template('eligible.html', name=name, eligibleCourses = allEligibleCourses, availableScienceCourses = availableScienceCourses, otherAvailableCourses = otherAvailableCourses, ineligible=ineligible)

            
            

            return render_template('eligible.html', name=name, eligibleCourses = allEligibleCourses, availableScienceCourses = availableScienceCourses, otherAvailableCourses = otherAvailableCourses, ineligible=ineligible)
            # return redirect('') 

        
        else:
            print(form.errors)
            sendtelegram("VALIDATION ERROR" + '\n' + str(form.errors))
            flash(f'There was a problem please try again','danger')



    if request.method == 'GET':
        print(form)
        eligibleCourses = []
        print("GET REQUESTS")
        mathsFromSession = "- -"

        # if session:
        #     print("session[maths]")
        #     print(session)
        #     try:
        #         print(session['mathematics-s'])
        #         mathsFromSession = session['mathematics-s']
        #         nameFromSession = session['name-s']
        #         numberFromSession = session['number-s']
        #         englishFromSession = session['english-s']
        #         scienceFromSession = session['science-s']
        #         socailFromSession = session['social-s']
        #         el1FromSession = session['el1-s']
        #         el1GradeFromSession = session['el1grade-s']
        #         el2FromSession = session['el2-s']


        #         el2GradeFromSession = session['el2grade-s']
        #         el3FromSession = session['el3-s']
        #         el3GradeFromSession = session['el3grade-s']
        #         el4FromSession = session['el4-s']
        #         el4GradeFromSession = session['el4grade-s']
        #         print("successful")
        #     except:
        #         print("asdf")
            



        # else:
        #     print("Filling fields")
        #     nameFromSession= ""
        #     numberFromSession= "--"
        #     mathsFromSession = "--"
        #     englishFromSession = "--"
        #     scienceFromSession = "--"
        #     socailFromSession = "--"
        #     el1FromSession = "--"
        #     el1GradeFromSession = "--"
        #     el2FromSession = "--"
        #     el2GradeFromSession = "--"
        #     el3FromSession = "--"
        #     el3GradeFromSession = "--"
        #     el4FromSession = "--"
        #     el4GradeFromSession = "--"

        print(eligibleCourses)
        return render_template('index.html', electives=electives, els=els, grades=grades, array=array,
        maths=mathsFromSession, english="englishFromSession", social="socailFromSession", science="scienceFromSession",
        electiveOne="el1FromSession", electiveOneGrade="el1GradeFromSession", electiveTwo="el2FromSession", electiveTwoGrade="el2GradeFromSession",
        electiveThree="el3FromSession", electiveThreeGrade="el3GradeFromSession", electiveFour="el4FromSession", electiveFourGrade="el4GradeFromSession",
        name="nameFromSession", number="numberFromSession", form=form
        )
    return render_template('index.html', electives=electives, els=els, grades=grades, array=array, form=form)
    
# 
def convertCourseToString(array):

    print('--- ARRAY ---')
    print(array)
    responseArray = []
    for course in array:
        print(course)
        if course is not None:
            responseArray.append({"name":course.name,"department":course.department,"tempField":course.tempField})

    print("SUCCESSFULL COURSE CONVERSION COMPLETE")

    print(responseArray)

    return responseArray

def sendtelegram(params):
    url = "https://api.telegram.org/bot1699472650:AAEso9qTbz1ODvKZMgRru5FhCEux_91bgK0/sendMessage?chat_id=-511058194&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content

@app.route("/eligible/<int:id>")
def eligible(id):
    eligibleCourses = []
    print(id)
    result = Results.query.get_or_404(id)
    print(result)
    print(result.passed)
    allEligibleCourses = result.eligibleCourses
    array = allEligibleCourses.split("' )")
    print(len(array))
    print(allEligibleCourses)
    print('--------')
    print(array[0])
    print(type(array))
    availableScienceCourses = result.availableScienceCourses
    otherAvailableCourses = result.otherAvailableCourses
    if result.passed != True:
        ineligible = True
    else:
        ineligible = False
    allEligCourses = []
    courseIds = json.loads(result.results)


    for course in courseIds:
        allEligCourses.append(Course.query.get_or_404(course))
    print(allEligCourses)

    
    # return render_template('eligible.html',eligibleCourses = eligibleCourses)
    return render_template('eligible.html', name=result.name, eligibleCourses = allEligCourses, availableScienceCourses = availableScienceCourses, otherAvailableCourses = otherAvailableCourses, ineligible=ineligible)


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

@app.route('/detail',methods=['GET','POST'])
def detail():
    return render_template("details.html")


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


@app.route("/results",methods=['GET','POST'])
def results(): 
    #  Use session
    results = Results.query.all()
    if request.method=='POST':
        password = request.form.get('password')
        print(password)
        if password == 'admin':
            return render_template('results.html', results=results, passed=True)
        else:
            flash(f'Wrong password, please try again','danger')
    else:
        return render_template('results.html', results=results)
    return render_template('results.html')


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