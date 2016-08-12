from peewee import *
from base import mysql_database
from amenity import Amenity
from place import Place

class PlaceAmenities(Model):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

    class Meta:
        database = mysql_database
