import peewee
import md5

database = peewee.SqliteDatabase("database",  pragmas=(('foreign_keys', True), ))
class USER (BaseModel):
    email = peewee.CharField(128, null=False, unique=True)
    password = peewee.CharField(128, null=False)
    first_name = peewee.CharField(128, null=False)
    last_name = peewee.CharField(128, null=False)
    is_admin = peewee.BooleanField(default=False)

    def set_password(self, clear_password):
        self.pasword = md5.new(clear_password).hexidigest()
