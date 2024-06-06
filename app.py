from flask import *
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

def read_json():
    with open('input.json', 'r') as file:
        data = json.load(file)
    return data


# endpoints
@app.route('/',methods=['GET'])

def index():
    return redirect('/schedules')

@app.route('/schedules', methods=['GET'])

def schedules():
    data = jsonify(read_json())
    data.headers.add('Access-Control-Allow-Origin', '*')
    data.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    data.headers.add('Access-Control-Allow-Methods', 'GET, POST')
    return data

if __name__ == '__main__':
    app.run()