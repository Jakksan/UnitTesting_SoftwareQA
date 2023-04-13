# To run, use $flask --app flaskr run --debug
import os

from flask import Flask, render_template, request
import sys
from pathlib import Path

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

import src.BMI.BMICalc as BMI

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!<br><form></form>'


    @app.route('/')
    def index():
        return(render_template('index.html'))

    # @app.route('/form')
    # def form():
    #     return(render_template('index.html'))
    
    @app.route('/data', methods = ['POST', 'GET'])
    def data():
        if request.method == 'GET':
            return f'{"The URL /data is accessed directly. Try going to /index to submit index"}'
        if request.method == 'POST':
            form_data = request.form
            weight = form_data["lbs"]
            height_ft = form_data["ft"]
            height_in = form_data["in"]
            bmi = BMI.findBMI(weight, height_ft, height_in, 3)
            bmi_class = BMI.classifyBMI(bmi)
            return render_template('index.html',bmi=bmi, bmi_class=bmi_class)
    

    return app