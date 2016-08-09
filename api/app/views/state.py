# from flask import jsonify
# from flask_json import request
# from peewee import *
# from app.models.state import State
# from app import app
#
# @app.route('/states/', methods =["GET", "POST"], strict_slashes=False)
# def app_states():
#     if request.method == "GET":
#         try:
#             query = State.select()
#             return jsonify([recored.to_hash() for record in query]), 200
#         except State.DoesNotExist:
#             return jsonify({"code": 404, "msg": "No tables exist yet"}), 404
#     elif request.method == "POST":
#         try:
#             new = State.create(
#                 name = str(request.form['name'])
#             )
#             return jsonify(new.to_hash()), 201
#         except:
#             return jsonify({"code": 10001, "msg": "State already exists"}), 409
#
# @app.route('/states/<state_id>', methods=["Get", "DELETE", strict_slashes=False])
# def app_states_id(state_id):
#     if request.method == "GET":
#         try:
#             query = State.get(State.id == state_id)
#             return jsonify(query.to_hash()), 200
#         except:
#             return jsonify({"code": 404, "msg": "not found"}), 404
#     elif request.method == "DELETE":
#         try:
#             query = State.get(State.id == state_id)
#             query.delete_instance()
#             return jsonify({"code": 200, "msg": "success"}), 200
#         except:
#             return jsonify({"code": 404, "msg": "not found"}), 404
