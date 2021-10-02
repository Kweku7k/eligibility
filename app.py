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
    # vendor = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    def __repr__(self): 
        return f"Course('{self.id}', '{self.name}', )"

@app.route('/',methods=['GET','POST'])
def home():
    electives = Course.query.all()
    grades = ['A1','B2','B3','C4','C5','C6','D7','E8','F9']

    if request.method=='POST':
        print('request.form')
        print(request.args)
        return redirect(url_for('eligible'))

    return render_template('index.html', electives=electives, grades=grades)

@app.route("/eligible",methods=['GET','POST'])
def eligible():
    return render_template('eligible.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)

