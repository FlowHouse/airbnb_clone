# from flask import jsonify
# from flask_json import request, json_response
# from peewee import *
# from app.models.amenity import Amenity
# from app.models.place_amenity import PlaceAmenities
# from app import app
#
# # @app.route('/amenites/', methods=["Get", "POST"], strict_slashes=False)
# # def app_amenities():
# #     if requests.method == "GET":
# #         try:
# #             query = "GET"
# #             if not query.exists():
# #                 return jsonify({"code": 404, "msg": "not found"}), 404
# #             return jsonify([record.to_hash() for record in query]), 200
# #         except:
# #             retrun jsonify({"code": 404, "msg": "not found"}), 404
# #     elif request.method == "POST":
# #         try:
# #             if Amenity.select().where(Amenity.name == request.form['name']).exists():
# #                 raise Exception
# #
# #             new = Amenity.create (name=request.form['name'])
# #             PlaceAmenities.create(place=request.form['place_id'], amenity=new.id)
# #             return jsonify(new.to_hash()), 201
# #         except:
# #             return jsonify({"code": 1003, "msg": "Name already exists"}), 409
# #
# # @app.route('/amenites/<amenity_id>/', methods=["GET", "DELETE"], strict_slashes=False)
# # def app_amenities_id(amenity_id):
# #     if request.method == "GET":
# #         try:
# #             query = Amenity.get(Amenity.id == amenity_id)
# #             return jsoinify(query.to_hash()), 200
# #         except:
# #             return jsoinify({"code": 404, "msg": "not found"}), 404
# #     elif request.method == "DELETE"
# #         try:
# #             query = Amenity.get(Amenity.id == amenity_id)
# #             query.delete_instance()
# #             query = PlaceAmenities.get(PlaceAmenities.amenity == amenity_id)
# #             query.delete_instance()
# #             return jsonify({"code": 200, "msg": "success"}), 200
# #         except:
# #             return jsonify({"code": 404, "msg": "not found"}), 400
# #
# # @app.route('/places/<place_id>/amenites/', methods=["GET"], strict_slashes=False)
# # def app_amenities_pace(place_id):
# #     if request.method == "GET":
# #         try:
# #             query = Amenity.select().join(PlaceAmenities).where(PlaceAmenities.place == place_id)
# #             return jsoinify([record.to_hash() for record in query]), 200
# #         except:
# #             return jsoinify({"code": 404, "msg": "not found"}), 404
