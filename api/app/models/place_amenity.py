from peewee import *
from base import mysql_database
from amenity import Amenity
from place import Place

class PlaceAmenities(peewee.Model):
    place = peewee.ForeignKeyField(Place)
    amenity = peewee.ForeignKeyField(Amenity)

    class Meta:
        database = mysql_database
