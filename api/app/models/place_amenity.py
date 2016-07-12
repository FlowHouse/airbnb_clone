import peewee
import amenity
import place

class PlaceAmenities(peewee.Model):
    place = peewee.ForeignKeyField(Place)
    amenity = peewee.ForeignKeyField(Amenity)
