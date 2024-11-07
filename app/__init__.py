from flask import Flask 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FORMS_DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "Yorseestrinuecretsing"


db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

print(db)

from app import routes
