import peewee
# hacky way of importing models
from app.models.amenity import *
from app.models.base import *
from app.models.city import *
from app.models.place_amenity import *
from app.models.place_book import *
from app.models.place import *
from app.models.state import *
from app.models.user import *

models = {
	'amenity': Amenity,
	'base': BaseModel,
	'city': City,
	'place_amenity': Place_amenity,
	'place_book': Place_book,
	'place': Place,
	'state': State,
	'user': User
}

mysql_database.connect()
mysql_database.create_tables([
	Amenity,Base,
	City,
	Place_amenity,
	Place_book,
	Place,
	State,
	User
])
