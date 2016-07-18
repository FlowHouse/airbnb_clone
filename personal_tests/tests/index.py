# test github pull from head to forked repo
import unittest
import datetime
import json
import requests
# import <app>

# to create a test client of app
def setUp(self):
	self.<DB_NAME>, <APP>.app.config['<DATABASE_NAME>'] = tempfile.mkstemp()
	<APP>.app.config['TESTING'] = True
	self.app = <APP>.app.test_client()
	with <APP>.app.app_context(): # not sure what this does
		<APP>.init_db()
# to validate if status of the JSON resp of GET / is equal to 200
def test_200(self):
	response = requests.get('http://localhost:5555/')
	assert response.status_code == 200

# to validate if status of the JSON resp of GET / is equal to OK
def test_status(self):
	response = requests.get('http://localhost:5555/')
	data = json.loads(response.text)
	assert data['status'] == 'OK'

# to validate if time of the JSON resp of GET / is equal of local time
def test_time(self):

# to validate if utc time of the JSON resp of GET / is equal of utc time
def test_time_utc(self):
