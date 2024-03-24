from flask import *

from slojno.project.generate_json import generate_json


@app.route('/')
def index():
    return send_file('files/sample_html.html')


@app.route('/content.json')
def index():
    return send_file(generate_json())


@app.route('/index.css')
def index():
    return send_file('files/1.css')
