from flask import *
from flask_json import *
from peewee import *
from datetime import datetime
from dateutil import tz
from app import app
from app.models.base import *
from MySQLDatabase import *

app.config['JSON_ADD_STATUS'] = False

@app.route('/', methods=['GET'])
@as_json
def index():
    json_response = {
		'status': "OK",
        'utc_time': str(datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S")),
        'time': str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	}
    return json_response

@app.before_request
def before_request():
    mysql_database.connect()

@app.after_request
def after_request(response):
    mysql_database.close()
    return response

@app.errorhandler(404)
def not_found(error):
    json_response = {
        'code': 404,
        'msg': "not found"
        }
        return json_response
