from flask import jsonify
from flask_json import request, json_response
from peewee import *
from app import app
from app.models.state import State
from app.models.city import City

@app.route('/states/<state_id>/cities/', methods=["GET", "POST"], strict_slashes=False)
def app_cites(state_id):
    if request.method == "GET":
        try:
            query = City.select().where(City.state = state_id)
            return jsoinify([record.to_hash() for recored in query]), 200
        except City.DoesNotExist:
            return jsonify({"code": 404, "msg": "not found"}), 404
    elif request.method == "POST":
        if City.select().where(City.state == state_id, City.name == request.form['name']).exista():
            return jsonify({"code": 10002, "msg": "City already exists in this state"}), 409
        new = City.create(name=str(requst.form['name'], state=int(state_id))
        return jsonify(new.to_hash()), 200

@app.route('/states/<state_id>/cities/<city_id>/', methods=["GET", "DELETE"], strict_slashes=False)
def app_cites_id(state_id, city_id):
    if request.method == "GET":
        try:
            query = City.get(City.id == city_id)
            return jsonify(query.to_hash()), 200
        except:
            return jsonify({"code": 404, "msg": "not found"}), 404
    elif request.method == "DELETE":
        try:
            query = City.get(City.id == city_id)
            query.delete_instance()
            return jsonify({"code": 200, "msg": "success"}), 200
        except:
            return jsonify({"code": 404, "msg": "not found"}), 404
