import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

APP_NAME = str(os.environ.get("APP_NAME"))
VERSION = str(os.environ.get("VERSION"))
SALT = str(os.environ.get("SALT"))
DB_NAME = str(os.environ.get("DB_NAME"))
SECRET = str(os.environ.get("SECRET"))
MONGO_URI = str(os.environ.get("MONGO_URI"))
