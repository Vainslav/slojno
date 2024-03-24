from flask import *
from markupsafe import escape

from generate_json import generate_json

app = Flask(__name__)
users_dict = {}


@app.route('/')
def index():
    if request.remote_addr not in users_dict.keys():
        users_dict[request.remote_addr] = {'1': 0, '2': 0, '3': 0}
    return send_file('file/index.html')


@app.route('/content.json')
def send_json():
    return generate_json()


@app.route('/file/<name>')
def send_f(name):
    print(name)
    print("safsadf")
    return send_file(f'file/{name}')

@app.route('/images/<name>')
def send_af(name):
    return send_file(f'file/images/{name}')


@app.route('/api/add/<id>', methods=["POST"])
def add_item():
    users_dict[request.remote_addr][id] += 1


@app.route('/api/sub/<id>', methods=["POST"])
def sub_item():
    users_dict[request.remote_addr][id] -= 1
