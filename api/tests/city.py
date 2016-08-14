from app import app
from app.models.state import State
from app.models.city import City
from app.models.base import *
import unittest
import logging
from peewee import *
import json

class city_test(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)
        self.app = app.test_client()
        mysql_database.connect()
        mysql_database.create_tables([State, City], safe=True)

    def tearDown(self):
        mysql_database.drop_tables([City, State], safe=True)

    def create_city(self, city_name):
        return self.app.post('/states/1/cities', data=dict(
            name=city_name,
            state=1
            ))

    def test_create(self):
        for i in range(3, 5):
            result = self.create_city("t_" + str(i))
            self.assertEqual(json.loads(result.data)['id'], i)
        no_parameter = self.app.post('/states/1/cities',
                                      data=dict(bad_param="test"))
        not_unique = self.create_city("test_2")

        self.assertEqual(no_parameter.status_code, 400)
        self.assertEqual(not_unique.status_code, 409)
        self.assertEqual(json.loads(not_unique.data)['code'], 10002)

        result = self.app.get('/states/1/cities')

if __name__ == '__main__':
    unittest.main()
