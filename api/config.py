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
