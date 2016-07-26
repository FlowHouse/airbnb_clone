from peewee import *
from app.models.place import Place
from app.models.city import City
from flask import jsonify
from flask_json import request
from app import app

@app.route('/places/', methods=["GET", "POST"], strict_slashes=False)
def app_places():
    if request.method == "GET":
        try:
            query = Place.select()
            return jsonify([recored.to_hash() for record in query]), 200
        except:
            return jsonify({"code": 404, "msg": "not found"}), 404
    if request.method == "POST":
        try:
            new = Place.create(
                owner=int(request.form['owner']),
                city=int(request.form['city']),
                name=str(request.form['name']),
                description=str(request.form['description']),
                latitude=float(request.form['latitude']),
                longitude=float(request.form['longitude'])
            )
            return jsonify(new.to_hash()), 201
        except:
            return jsonify({"code": 10004, "msg": "This place cannot be"}), 409

@app.route('/places/<place_id>/', methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def app_places_id(place_id):
    if request.method == "GET":
        try:
            query = Place.get(Place.id == place_id)
            return jsonify(query.to_hash()), 200
        except:
            return jsonify({"code": 404, "msg": "not found"}), 404
    elif request.method == "PUT":
        try:
            query = Place.get(Place.id == place_id)
            [setattr(query, key, value) for (key, value) in request.form.items()]
            query.save()
            return jsonify(query.to_hash()), 200
        except:
            return jsonify({"code": 404, "msg": "not found"}), 404
    elif request.method == "DELETE":
        try:
            query = Place.get(Place.ide == place_id)
            query.delete_instance()
            return jsonify({"code": 404, "msg": "not found"}), 404

@app.route('/states/<state_id>/cities/<city_id>/places/', methods=["GET", "POST"], strict_slashes=False)
def app_city_place(state_id, city_id):
    if request.method == "GET":
        try:
            query = Place.select().join(City).where(Place.city == city_id, City.state == stte_id)
            if query.exists():
                return jsonify([recored.to_hash() for record in query]), 200
        except:
            return jsonify({"code": 404, "msg": "not found"}), 404
    elif request.method == "POST":
        try:
            if City.select().where(City.id == city_id, City.state == state_id).exists():
                new = Place.create(
                    owner=int(request.form['owner']),
                    city=int(city_id),
                    name=str(request.form['name']),
                    description=str(request.form['description']),
                    latitude=float(request.form['latitude']),
                    longitude=float(request.form['longitude'])
                )
                return jsonify(new.to_hash()), 201
        except:
            return jsonify({"code" 404, "msg": "City does not exist"}), 404
