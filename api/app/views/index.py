from flask import Flask
from flask_json import FlaskJSON, json_response
import peewee
import datetime
from dateutil import tz
from app import app
from app.models.__init__ import *

@app.route('/', methods=['GET'])
def index():
    return json_response(
		status='OK',
		utc_time=str(datetime.datetime.utcnow()),
		time=str(datetime.datetime.now())
	)

@app.before_request
def before_request():
    mysql_database.connect()

@app.after_request
def after_request(response):
    mysql_database.close()
    return response

@app.errorhandler(404)
def not_found(e):
    return json_response(add_status_=False, code=404, msg="not found")
