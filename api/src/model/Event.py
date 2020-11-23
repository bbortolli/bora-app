from mongoengine import *
import datetime

class Event(Document):
  name = StringField(max_length=100, required=True)
  city = StringField(min_length=24, max_length=24, required=True)
  state = StringField(min_length=24, max_length=24)
  country = StringField(min_length=24, max_length=24)
  date = DateTimeField()
  created_at = DateTimeField(default=datetime.datetime.utcnow)
