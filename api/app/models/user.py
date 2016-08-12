from peewee import *
from base import BaseModel
import hashlib
import md5

# database = peewee.SqliteDatabase("database",  pragmas=(('foreign_keys', True), ))


class User (BaseModel):
    email = CharField(128, null=False, unique=True)
    password = CharField(128, null=False)
    first_name = CharField(128, null=False)
    last_name = CharField(128, null=False)
    is_admin = BooleanField(default=False)
    # if not email:
    # 	return json_response(users)
	# else:
    # 	return json_response(code= 1000, msg="Email already exists")

    def set_password(self, clear_password):
        self.pasword = hashlib.md5.new(clear_password).hexidigest()

    def to_hash(self):
        hash = {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_admin": self.is_admin,
        }
        return hash
