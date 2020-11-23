from mongoengine import *
import datetime

class Group(Document):
    name = StringField(max_length=100, required=True)
    origin = StringField(max_length=100, required=True)
    destiny = StringField(max_length=100, required=True)
    owner = StringField(min_length=24, max_length=24, required=True)
    managers = ListField(StringField(min_length=24, max_length=24))
    members = ListField(StringField(min_length=24, max_length=24))
    requests = ListField(StringField(min_length=24, max_length=24))
    invites = ListField(StringField(min_length=24, max_length=24))
    created_at = DateTimeField(default=datetime.datetime.utcnow)
