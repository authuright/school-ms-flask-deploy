# third party import
import os
from flask import Flask

# package import

app = Flask(__name__)  

@app.route('/')
def index():
    return "Hello World"

@app.route('/dashboard')
def dashboard():
    return "Hello Flask"


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)