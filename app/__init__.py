from flask import Flask 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import os


app = Flask(__name__)


<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:new_password@45.222.128.55:5432/eligibility'
=======
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FORMS_DB_URL')
>>>>>>> 6b9e95a22e719fa0ebaa4f55e47ff42c65d75710
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "Yorseestrinuecretsing"


db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

print(db)

from app import routes
