from app import app
from app.models import *


if __name__ == '__main__':
    #DEBUG is SET to TRUE. Laughing out louyd CHANGE FOR PROD
    # app.run(port=5000,debug=True)
    # app.secret_key='12345'
    app.run(host='0.0.0.0', debug=True)

    