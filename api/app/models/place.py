import peewee
import user
import city

class Place(BaseModel):
    owner = peewee.ForeignKeyField(User, related_name = "places")
    city = peewee.ForeignKeyField(User, related_name = "places")
    name = peewee.CharField(128, null=False)
    description = TextField()
    number_rooms = IntegerField(default = 0)
    number_bathrooms = IntegerField(default = 0)
    max_guest = IntegerField(default = 0)
    price_by_night = IntegerField(default = 0)
    latitude = FloatField()
    longitude = FloatField()
