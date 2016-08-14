import peewee
from config import *
from datetime import datetime

'''
=======================
base python starts here
=======================
'''
mysql_database = peewee.MySQLDatabase(
	user=DATABASE['user'],
	passwd=DATABASE['password'],
	host=DATABASE['host'],
	charset=DATABASE['charset'],
	port=DATABASE['port'],
	database=DATABASE['database']
)

class BaseModel(peewee.Model):
	"""docstring for BaseModel"""

	id = peewee.PrimaryKeyField(unique = True)
	created_at = peewee.DateTimeField(default=datetime.now)
	updated_at = peewee.DateTimeField(default=datetime.now)


	# save func TODO more comments
	def save(self, *args, **kwargs):
		self.update_at = datetime.now()
		return super(BaseModel, self).save(*args, **kwargs)

	# metaclass func
	class Meta():
		database = mysql_database
		ordered_by = ("id", )
