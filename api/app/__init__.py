from flask import Flask
from flask_json import FlaskJSON
import config

__all__ = ["coinfig"]

app = Flask(__name__)
FlaskJSON(app)
