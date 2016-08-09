# from flask import jsonify
# from flask_json import request, json_response
# from peewee import *
# from app.models.user import User
# from app import app
#
# # users = []
#
# @app.route('/users', methods=['GET', "POST"], strict_slashes=False)
# def list_users():
# 	if request.method = "GET":
# 		query = User.select()
# 		return jsonify([record.to_hash() for record in query]), 200
#
# 	elif request.method == "POSt":
# 		try:
# 			new = User.create (
# 				email=str(request.form['email']),
#                 first_name=str(request.form['first_name']),
#                 last_name=str(request.form['last_name']),
#                 password=""
# 			)
# 			new.set_password(str(request.form['password']))
# 			return jsonify(new.to_hash()), 201
#
# @app.route('/users/<user_id>', methods=['GET', "PUT", "DELETE"], strict_slashes=False)
# def list_user_by_id(user_id):
# 	if request.method == "GET":
# 		try:
# 			query = User.get(User.id = user_id)
# 			return jsonify(query.to_hash())
# 		except User.DoesNotExist:
# 			return jsonify({"code": 404, "msg": "not found"}), 404
# 	elif request.method == "PUT":
# 		try:
# 			query = User.get(User.id == user_id)
# 			[setattr(query, key, value) for (key, value) in request.form.items()]
# 			query.save()
# 			return jsonify(query.to_hash()), 200
# 		except:
# 			return jsonify({"code": 404, "msg": "not found"}), 404
#
# 	elif request.method = "DELETE":
# 		try:
# 			query = User.get(User.id == user_id)
# 			query.delete_instance()
# 			return jsonify({"code": 200, "msg": "sucess"}), 200
# 		except:
# 			return jsonify({"code": 404, "msg": "not found"}), 404
