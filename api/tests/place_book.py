from app.models.base import *
from app.models.place_book import PlaceBook
from app.views.user import *
from app import app
import unittest
import logging
import json

class test_place_book(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        logging.disable(logging.CRITICAL)
        mysql_database.connect()
        mysql_database.create_tables([PlaceBook], safe=True)

    def tearDown(self):
        mysql_database.drop_table(PlaceBook)

if __name__ == '__main__':
    unittest.main()
