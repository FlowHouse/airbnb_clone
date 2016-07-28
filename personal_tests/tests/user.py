from app.models.base import mysql_database
from app.models.user import User
from app.views.user import *
from app import app
import unittest
import logging

class test_user(unittest.TestCase):
