from app import app
from app.models import *


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)

    