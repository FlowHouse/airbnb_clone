from app.models.base import *
from app.models.amenity import Amenity
from app.views.user import *
from app import app
import unittest
import logging
import json

class test_amenity(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        mysql_database.connect()
        mysql_database.create_tables([Amenity], safe=True)

    def tearDown(self):
        mysql_database.drop_table(Amenity)

if __name__ == '__main__':
    unittest.main()
