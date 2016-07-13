import peewee
from datetime import datetime
from config import *

'''
=======================
base python starts here
=======================
'''

class BaseModel(peewee.Model):
	"""docstring for BaseModel"""
	# init func
	def __init__(self):
		# TODO

	# unique id for tables
	id = peewee.PrimaryKeyField(unique = True)
    update_at = peewee.DateTimeField(default = datetime.now().strftime('%Y/%m/%d %H:%M;%S'))
    create_at = peewee.DateTimeField(default = datetime.now().strftime('%Y/%m/%d %H:%M;%S'))

	# save func TODO more comments
    def save(self, *args, *kwargs):
        self.update_at = datetime.now().strftime('%Y/%m/%d %H:%M;%S')
        peewee.Model.save(self)

	# metaclass func
    class Meta():
        database = mysql_database
        ordered_by = ("id", )
