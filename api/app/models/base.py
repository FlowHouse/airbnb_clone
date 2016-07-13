import peewee
from datetime import datetime
#import config

'''
=============================================
copy paste from config.py until more is known
=============================================
'''
# TODO ===V===

ENV = os.environ.get('AIRBNB_ENV', '')

# DEV
if ENV == 'development':
	DEBUG = True
	HOST = localhost
	PORT = 3333
	DATABASE = {
		'host': # IP address for web-01,
		'user':'airbnb_user_dev',
		'database': 'airbnb_dev',
		'port': 3306,
		'charset': 'utf8',
		'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV', '')
	}
# PROD
else if ENV == 'production':
	DEBUG = False
	HOST = 0.0.0.0
	PORT = 3000
	DATABASE = {
		'host': # IP address for web-01,
		'user':'airbnb_user_prod',
		'database': 'airbnb_prod',
		'port': 3306,
		'charset': 'utf8',
		'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD', '')
	}
# ERRORS
else:
	raise Exception("Sum Ting Wong")

'''
=======================
base python starts here
=======================
'''


# init the database with the correct parameters
mysql_database = peewee.MySQLDatabase(
	DATABASE.get('database'),
	user=DATABASE.get('user'),
	password=DATABASE.get('password'),
	host=DATABASE.get('host'),
	charset=DATABASE.get('charset')
)

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
