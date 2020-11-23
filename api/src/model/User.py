from mongoengine import *
import datetime
from src.model.sets import STATES, COUNTRIES, GENDERS

class User(Document):
  email = EmailField(required=True, unique=True)
  first_name = StringField(max_length=100, required=True)
  last_name = StringField(max_length=100, required=True)
  password = StringField(max_length=500, required=True)
  city = StringField(min_length=2, max_length=100, required=True)
  state = StringField(choices=STATES)
  country = StringField(choices=COUNTRIES)
  document = StringField(min_length=5, max_length=50)
  gender = StringField(choices=GENDERS)
  birthday = DateTimeField(min_length=24, max_length=24)
  friends = ListField(StringField(min_length=24, max_length=24))
  groups = ListField(StringField(min_length=24, max_length=24))
  events = ListField(StringField(min_length=24, max_length=24))
  invites = ListField(StringField(min_length=24, max_length=24))
  created_at = DateTimeField(default=datetime.datetime.utcnow)
