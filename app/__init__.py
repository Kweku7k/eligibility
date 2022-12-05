from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@eligibility.central.edu.gh:5432/elDb'
# password = 'password'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:'+password+'@eligibility.central.edu.gh:5432/elDb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "Your_secret_string"

from app import routes


