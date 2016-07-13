import peewee
from config import *

# init the database with the correct parameters
mysql_database = peewee.MySQLDatabase(
	DATABASE.get('database'),
	user=DATABASE.get('user'),
	password=DATABASE.get('password'),
	host=DATABASE.get('host'),
	charset=DATABASE.get('charset')
)
