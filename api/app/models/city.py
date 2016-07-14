import peewee
import state


class City(BaseModel):
    name = peewee.CharField(128, null=False)
    state = peewee.ForeignKeyField(state, related-name= 'cities', on_delete = "CASCADE")

    def to_hash(self):
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "name": self.__name,
            "state_id": self.__state_id, => ID of the State linked
        }
