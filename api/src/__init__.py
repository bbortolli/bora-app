from flask import Flask
from flask_cors import CORS, cross_origin
from mongoengine import connect
from cfg.settings import MONGO_URI

connect('bora-app-db', host=MONGO_URI)

app = Flask(__name__)
CORS(app)

import src.routes
