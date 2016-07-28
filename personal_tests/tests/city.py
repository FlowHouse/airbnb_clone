from app import app
from app.models.state import state
from app.models.city import City
from app.models.base import BaseModel
import unittest
import logging

class city_test(unitest.TestCase):

    def sertup(self):
        logging.disable(logging.CRITICAL)
        self.app = app.test_client()
        mysql_database.connect()
        mysql_database.creat_tables([State, City])

    def tearDown(self):
        mysql_database.drop_tables([State, City])

    def test_create(self):
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 200
        print new_state.status_code
        new_city = self.app.post('/states/1/cities', data=dict(name='San Francisco'))
        assert new_city.status_code == 200
