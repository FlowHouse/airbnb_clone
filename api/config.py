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
		'pasword': os.environ.get('AIRBNB_DATABASE_PWD_DEV', '')
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
		'pasword': os.environ.get('AIRBNB_DATABASE_PWD_PROD', '')
	}
