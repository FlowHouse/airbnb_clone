# from peewee import *
# from app.models.place_book import PlaceBook
# from flask import jsonify
# from flask_json import request
# from app import app
# from datetime import datetime
#
# @app.route('/places/<place_id>/books/', methods=["GET", "POST"], strict_slashes=False)
# def app_books(place_id):
#     if requests.method == "GET":
#         try:
#             query = PlaceBook.select().where(PlaceBook.place == place_id)
#             if not query.exists():
#                 raise Exception
#             return jsonify([record.to_hash() for record in query]), 200
#         except:
#             return jsonify({"code": 404, "msg": "not found"}), 404
#     elif request.method == "POST":
#         try:
#             dt_start = datetime.strptime(request.form['date_start'], '%Y/%m/%d %H:%M:%S')
#         except ValueError:
#             return jsonify({"code": 400, "msg": "improper date format"}), 400
#         try:
#             new = PlaceBook.create(
#                 place=int(place_id),
#                 user=int(request.form['user']),
#                 date_start=dt_start
#             )
#             return jsonify(new.to_hash()), 200
#         except:
#             return jsonify({"code": 10006, "msg": "Booking error: place or user may not yet exist"}), 409
#
# @app.route('/places/<place_id>/books/<book_id>/', methods=["GET", "PUT", "DELETE"], strict_slashes=False)
# def app_books_id(place_id, book_id):
#     if request.method == "GET":
#         try:
#             query = PlaceBook.get(PlaceBook.id == book_id)
#             return jsonify(query.to_hash()), 200
#         except:
#             return jsonify({"code": 404, "msg": "not found"}). 404
#     elif request.method == "PUT":
#         try:
#             query = PlaceBook.get(PlaceBook.id == book_id)
#             [setattr(query, key, value) for (key, value) in request.form.items()]
#             query.save()
#             return jsonify(query.to_hash()), 200
#         except:
#             return jsonify({"code": 404, "msg": "not found"}), 404
#     elif request.method == "DELETE":
#         try:
#             query = PlaceBook.get(PlaceBook.id == book_id)
#             query.delete_instance()
#             return jsonify({"code": 200, "msg": "success"}), 200
#         except:
#             return jsonify({"code": 404, "msg": "not found"}), 404
