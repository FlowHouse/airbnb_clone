from flask import Flask
from flask_json import FlaskJSON, json_response
import peewee
from app import app

@app.route('/users', methods=['GET'])
def list_users():
	return json_response(test='test')

@app.route('/users', methods=['POST'])
def create_user():
	return json_response(test='test')

@app.route('/users/<user_id>', methods=['GET'])
def list_user_by_id():
	pass

@app.route('/users/<user_id>', methods=['PUT'])
def update_user_by_id():
	pass

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id():
	pass
