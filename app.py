from flask import Flask

import mymath
from mymath import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    powerString = str(mymath.power(3,4))
    return f'Hello World! The answer is: {powerString}'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)