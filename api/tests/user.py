from app.models.base import *
from app.models.user import User
from app.views.user import *
from app import app
import unittest
import logging
import json
import time

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
        result = self.app.get('/users')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 0)

        for i in range(1, 16):
            self.create_user("test_" + str(i), "test_" + str(i),
                             "test_" + str(i), "test_" + str(i))

        result = self.app.get('/users')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 10)

        result = self.app.get('/users?page=2&number=10')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 5)
        self.assertEqual(
            json.loads(result.data)[1]['paging']['next'], None)

        result = self.app.get('/users?page=1&number=10')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 10)
        self.assertEqual(
            json.loads(result.data)[1]['paging']['previous'], None)

        result = self.app.get('/users?page=2&number=2')
        self.assertNotEqual(
            json.loads(result.data)[1]['paging']['next'], None)
        self.assertNotEqual(
            json.loads(result.data)[1]['paging']['previous'], None)

    def test_get(self):
        result = self.create_user("user_1", "user_1", "user_1", "user_1")
        self.assertEqual(result.status_code, 201)

        result = self.app.get('/users/1')
        self.assertEqual(json.loads(result.data)['first_name'], "user_1")

        result = self.app.get('/users/2')
        self.assertEqual(result.status_code, 404)

    def test_delete(self):
        result = self.create_user("user_1", "user_1", "user_1", "user_1")
        self.assertEqual(result.status_code, 201)

        result = self.app.get('/users')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 1)

        self.app.delete('/users/1')
        result = self.app.get('/users')
        self.assertEqual(len(json.loads(result.data)[0]['data']), 0)

        result = self.app.delete('/users/1')
        self.assertEqual(result.status_code, 404)

    def test_update(self):
        result = self.create_user("user_1", "user_1", "user_1", "user_1")
        self.assertEqual(result.status_code, 201)

        time.sleep(2)

        result = self.app.put('/users/1', data=dict(
            first_name="updated",
            last_name="updated",
            created_at="1989/07/10 22:00:00",
            updated_at="1989/07/10 22:00:00"
        ))

        self.assertEqual(result.status_code, 201)
        result = self.app.get('/users')

        self.assertNotEqual(json.loads(result.data)[0]['data'][0]['updated_at'],
                            "1989/07/10 22:00:00")
        self.assertNotEqual(json.loads(result.data)[0]['data'][0]['created_at'],
                            "1989/07/10 22:00:00")

        self.assertNotEqual(json.loads(result.data)[0]['data'][0]['created_at'],
                            json.loads(result.data)[0]['data'][0]['updated_at'])

        keys = ["first_name", "last_name"]
        for key in keys:
            self.assertEqual(json.loads(result.data)[0]['data'][0][key],
                             "updated")

        result = self.app.put('/users/2', data=dict(
            first_name="updated",
            last_name="updated",
        ))
        self.assertEqual(result.status_code, 404)

        result = self.app.put('/users/1', data=dict(
            email="updated"
        ))
        self.assertEqual(result.status_code, 409)


if __name__ == '__main__':
    unittest.main()
