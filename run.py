from app import app
from app.models import *
from flask_cors import CORS, cross_origin



if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)

    