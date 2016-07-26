from peewee import *
from base import BaseModel
from state import State


class City(BaseModel):
    name = peewee.CharField(128, null=False)
    state = peewee.ForeignKeyField(state, related_name= 'cities', on_delete = "CASCADE")

    def to_hash(self):
        hash = {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "name": self.name,
            "state_id": State.id,
        }
        return hash
