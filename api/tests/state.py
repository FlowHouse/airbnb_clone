from app.models.base import *
from app.models.state import State
from app import app
import unittest
import logging
import json

class test_state(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        mysql_database.connect()
        mysql_database.create_tables([State], safe=True)

    def tearDown(self):
        mysql_database.drop_tables([State])

    def create_state(self, state_name):
        return self.app.post('/states', data=dict(
            name=state_name
            ))

    def test_create(self):
        for i in range (1, 3):
            result = self.create_state("t_" + str(i))
            self.assertEqual(json.loads(result.data)['id'], i)
        no_parameter = self.app.post('/stats', data=dict(no_param="test"))
        not_unique = self.create_state("test_2")
        self.assertEqual(no_parameter.status_code, 400)
        self.assertEqual(not_unique.status_code, 409)

    def test_list(self):
        result = self.app.get('/stats')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 0)

        self.create_state("test")
        result = self.app.get('/states')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 1)

    def test_delete(self):
        result = self.create_state("test")
        self.assertEqual(result.status_code, 201)

        result = self.app.get('/states')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 1)

        self.app.delete('/states/1')
        result = self.app.get('/states')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 0)

        result = self.app.delete('/states/1')
        self.assertEqual(result.status_code, 404)
