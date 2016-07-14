import peewee
import md5

# database = peewee.SqliteDatabase("database",  pragmas=(('foreign_keys', True), ))


class USER (BaseModel):
    email = peewee.CharField(128, null=False, unique=True)
    password = peewee.CharField(128, null=False)
    first_name = peewee.CharField(128, null=False)
    last_name = peewee.CharField(128, null=False)
    is_admin = peewee.BooleanField(default=False)
    if email is
    return json_response(users)
    return json_response(code= 1000, msg="Email already exists")

    def set_password(self, clear_password):
        self.pasword = md5.new(clear_password).hexidigest()

    def to_hash(self):
        return {
            "id": self.__id,
            "created_at": self.__created_at,
            "updated_at": self.__updated_at,
            "email": self.__email,
            "first_name": self.__first_name
            "last_name": self.__last_name
            "is_admin": self.__is_admin,
        }
