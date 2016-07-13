import peewee
import place
import user

@app.route()
class PlaceBook(BaseModel):
    place = peewee.ForeignKeyField(Place)
    user = peewee.ForeignKeyField(User, related_name = "placesbooked")
    is_validated = peewee.BooleanField(default=False)
    date_start = peewee.DateTimeField(null = False)
    number_nights = peewee.IntegerField(default = 1)
