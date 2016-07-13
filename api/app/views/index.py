from flask import Flask
from flask_json import FlaskJSON, json_response
import peetwee

@app.route('/', methods=['GET'])
def index():

@app.errorhandler(404)
def before_request():
    models.database.connect()

def after_request():
    models.database.close()
    return response

def not_found():
    return json_response(add_status_=False, code=404, msg="response not found")
