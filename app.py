from flask import *
import json

app = Flask(__name__)


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
    data = read_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)