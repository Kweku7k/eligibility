from app import app
from app.models import *


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    # app.run(port=5000,debug=True)
    app.run(host='0.0.0.0')

    