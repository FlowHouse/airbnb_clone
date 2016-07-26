from peewee import *
from config import *
from datetime import datetime

'''
=======================
base python starts here
=======================
'''
mysql_database = peewee.MySQLDatabase(
	user=DATABASE['user']
	passwd=DATABASE['password'],
	host=DATABASE['host'],
	charset=DATABASE['charset'],
	port=DATABASE['port'],
	database=DATABASE['database']
)

class BaseModel(peewee.Model):
	"""docstring for BaseModel"""
	# init func
	def __init__(self):
		# TODO

	# unique id for tables
	id = peewee.PrimaryKeyField(unique = True)
	time = datetime.now().strftime('%Y/%m/%d %H:%M;%S')
	create_at = time
	updated_at = time

	# save func TODO more comments
    def save(self, *args, *kwargs):
        self.update_at = datetime.now().strftime('%Y/%m/%d %H:%M;%S')
        return super(BaseModel, self).save(*args, **kwargs)

	# metaclass func
    class Meta():
        database = mysql_database
        ordered_by = ("id", )
