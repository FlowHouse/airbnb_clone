from __init__ import app
from views.index import *
from config import HOST, PORT, DEBUG

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
