from app.__init__ import app
from config import *
from app.views import *

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
