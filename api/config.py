ENV = $AIRBNB_ENV

# DEV
if condition:
	DEBUG = True
	HOST = localhost
	PORT = 3333
	DATABASE = {
		host = # IP address for web-01
		user = 'airbnb_user_dev'
		database =
	}
# PROD
else:
	DEBUG: FALSE
	HOST: 0.0.0.0
	PORT: 3000
	DATABASE: {
		'host': # 158.69.91.82,
		'user': 'airbnb_user_prod',
		'database': 'airbnb_prod',
		'port': 3006,
		'charset': utf8,
		'password': os.environ.get('AIRBNB_DATABASE_PWD_PROD', ' ')

	}
