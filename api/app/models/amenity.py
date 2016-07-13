import peewee

@app.route()
class Amenity(BaseModel):
    name = peewee.CharField(128, null=False)
