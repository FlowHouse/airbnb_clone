import Peewee as peewee
from datetime import datetime
#import config

database = pw.MySQLDatabase('')

class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique = True)
    update_at = peewee.DateTimeField(defalt = datetime.now().strftime('%Y/%m/%d %H:%M;%S'))
    create_at = peewee.DateTimeField(defalt = datetime.now().strftime('%Y/%m/%d %H:%M;%S'))

    def save(self, *args, *kwargs):
        self.update_at = datetime.now().strftime('%Y/%m/%d %H:%M;%S')
        peewee.Model.save(self)


    class Meta():
        database = db
        ordered_by = ("id", )
