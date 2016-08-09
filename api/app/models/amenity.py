from peewee import *
from base import BaseModel


class Amenity(BaseModel):
    name = CharField(128, null=False)

    def to_hash(self):
        hash = {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "name": self.name,
        }
        return hash
