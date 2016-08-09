from app import app
from config import *
from app.views import *
from app.models import *

if __name__ == '__main__':
	app.run(host=HOST, port=PORT, debug=DEBUG)
