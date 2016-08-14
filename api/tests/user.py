from app.models.base import *
from app.models.user import User
from app.views.user import *
from app import app
import unittest
import logging
import json

class test_user(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        mysql_database.connect()
        mysql_database.create_tables([User], safe=True)

    def tearDown(self):
        mysql_database.drop_table(User)

    def create_user(self, first_name, last_name, email, password):
        return self.app.post('/users', data=dict(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        ))

    def test_create(self):
        for i in range(1, 3):
            results = self.create_user("test", str(i), str(i), str(i))
            self.assertEqual(json.loads(results.data)['id'], i)

        no_parameter = self.app.post('/users', data=dict(first_name="test"))
        not_unique = self.create_user("test", str(i), str(i) ,str(i))
        self.assertEqual(no_parameter.status_code, 400)
        self.assertEqual(not_unique.status_code, 409)

    def test_list(self):
        result = self.app.get('/user')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 0)

        self.create_state("test")
        result = self.app.get('/user')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 1)

    def test_get(self):
        pass

    def test_delete(self):
        pass

    def test_update(self):
        pass


if __name__ == '__main__':
    unittest.main()
