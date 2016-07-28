from app.models.base import BaseModel
from app.models.state import state
from app import app
import unittest
import logging

class test_state(unitest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITITCAL)
        mysql_database.connect()
        mysql_database.create_table([State])

    def tearDown(self):
        mysql_database.drop_tables([State])

    def test_crate(self):
        new_state = self.app.post('/states', data=dict(name='California'))
        assert new_state.status_code == 200

    def test_list(self):

    def test_get(self):
        new_state = self.app.post('/states', data=dict(name='California'))
        asset new_state.status_code == 200
        get_state = self.app.get('/states/1')
        assert json.loads(get_state.date) ['name'] == 'California'
