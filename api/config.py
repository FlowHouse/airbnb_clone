import os

ENV = os.environ.get('AIRBNB_ENV', '')

# DEV
if ENV == 'development':
	DEBUG = True
	HOST = '127.0.0.1'
	PORT = 3333
	DATABASE = {
		'host': '158.69.91.82',# IP address for web-01
		'user':'airbnb_user_dev',
		'database': 'airbnb_dev',
		'port': '3306',
		'charset': 'utf8',
		'password': os.environ.get('AIRBNB_DATABASE_PWD_DEV', '')
	}
# PROD
elif ENV == 'production':
	DEBUG = False
	HOST = '0.0.0.0'
	PORT = 3000
	DATABASE = {
		'host': '158.69.91.82',# IP address for web-01,
		'user':'airbnb_user_prod',
		'database': 'airbnb_prod',
		'port': '3306',
		'charset': 'utf8',
		'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD', '')
	}
# ERRORS
else:
	raise Exception("Sum Ting Wong")
