# test github pull from head to forked repo
import unittest
from datetime import datetime
import json
import time
import requests
from app import app

class BaseTest(unittest.TestCase):
	# """docstring for BaseTest"""
	# response = requests.get('http://127.0.0.1:5555/')

	# to create a test client of app
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True

	# to validate if status of the JSON resp of GET / is equal to 200
	def test_200(self):
		results = self.app.get('/')
		self.assertEqual(results.status_code, 200)

	# to validate if status of the JSON resp of GET / is equal to OK
	def test_status(self):
		results = self.app.get('/')
		d = json.loads(results.data)['status']
		self.assertEqual(d, 'OK')

	# to validate if time of the JSON resp of GET / is equal of local time
	def test_time(self):
		dt = self.app.get('/')
		time = str(json.loads(dt.data)['time'])
		t_compare = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
		self.assertEqual(time, t_compare)

	# to validate if utc time of the JSON resp of GET / is equal of utc time
	def test_time_utc(self):
		dt = self.app.get('/')
		utc_time = str(json.loads(dt.data)['utc_time'])
		utc_t_compare = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
		self.assertEqual(utc_time, utc_t_compare)

if __name__ == '__main__':
	unittest.main()
