import peewee


class Amenity(BaseModel):
    name = peewee.CharField(128, null=False)
