import peewee


class State(BaseModel):
    name = CharField(128, null = False, unique = True)

    def to_hash(self):
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "name": self.__name,
        }
