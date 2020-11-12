from flask import Flask
import pymongo
from cfg.settings import DB_NAME, MONGO_URI

client = pymongo.MongoClient(MONGO_URI)
db_session = client[DB_NAME]

app = Flask(__name__)

import src.routes
