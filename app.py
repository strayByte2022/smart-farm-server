from flask import *
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)


def read_json():
    with open('input.json', 'r') as file:
        data = json.load(file)
    return data


def write_json(data):
    with open('input.json', 'w') as file:
        json.dump(data,file, indent=4)


# endpoints
@app.route('/', methods=['GET'])
def index():
    return redirect('/schedules')


@app.route('/schedules', methods=['GET'])
def schedules():
    data = jsonify(read_json())
    print(type(data))
    data.headers.add('Access-Control-Allow-Origin', '*')
    data.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    data.headers.add('Access-Control-Allow-Methods', 'GET, POST')
    return data


@app.route('/schedules/<string:scheduler_name>/active', methods=['PUT'])
def update_schedule_active_state(scheduler_name):
    data = read_json()
    schedule = next((item for item in data if item["schedulerName"] == scheduler_name), None)
    if schedule is None:
        return abort(404, description='Schedule not found')
    if 'isActive' not in request.json:
        abort(400,description='No active schedule')

    schedule['isActive'] = request.json['isActive']
    write_json(data)
    return jsonify(schedule)


if __name__ == '__main__':
    app.run()
