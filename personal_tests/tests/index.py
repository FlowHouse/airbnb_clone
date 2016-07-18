# test github pull from head to forked repo
import unittest
import datetime
import json
import requests
from app import *

class BaseTest(unittest.TestCase):
	"""docstring for BaseTest"""
	response = requests.get('http://127.0.0.1:5555/')

	# to create a test client of app
	def setUp(self):
		self.app = app.test_client()

	# to validate if status of the JSON resp of GET / is equal to 200
	def test_200(self):
		assert response.status_code == 200

	# to validate if status of the JSON resp of GET / is equal to OK
	def test_status(self):
		data = json.loads(response.text)
		assert data['status'] == 'OK'

	# to validate if time of the JSON resp of GET / is equal of local time
	def test_time(self):
		dt = str(datetime.datetime.now())
		data = json.loads(response.text)
		assert data['time'] == dt

	# to validate if utc time of the JSON resp of GET / is equal of utc time
	def test_time_utc(self):
		dt = str(datetime.datetime.utcnow())
		data = json.loads(response.text)
		assert data['utc_time'] == dt

if __name__ == '__main__':
	unittest.main()
