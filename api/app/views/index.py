from flask import Flask
from flask_json import FlaskJSON, json_response
import peewee
import datetime
from dateutil import tz
from __init__ import *
from app import *
from app.models import *
from config import *
# HERE = tz.tzlocal()
# UTC = tz.gettz('UTC')

@app.route('/', methods=['GET'])
def index():
    return json_response(
		status='OK',
		utc_time=str(datetime.datetime.utcnow()),
		time=str(datetime.datetime.now())
		# utc_time=datetime(tzinfo=UTC).strftime('%m/%d/%Y %H:%M:%S'),
		# time=datetime(tzinfo=tzlocal()).strftime('%m/%d/%Y %H:%M:%S')
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

# def utc_to_local(utc_dt):
#     local_dt = utc_dt.replace(tzinfo=utc).astimezone(local_tz)
#     return local_tz.normalize(local_dt)
