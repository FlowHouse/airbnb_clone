import peewee
import place
from user import *
from place import Place


class PlaceBook(BaseModel):
    place = peewee.ForeignKeyField(Place)
    user = peewee.ForeignKeyField(User, related_name = "placesbooked")
    is_validated = peewee.BooleanField(default=False)
    date_start = peewee.DateTimeField(null = False)
    number_nights = peewee.IntegerField(default = 1)

    def to_hash(self):
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "place_id": Place.id,
            "user_id": User.id,
            "is_validated": self.__is_validated,
            "date_start": self.__date_start,
            "number_nights": self.__number_nights,
        }
