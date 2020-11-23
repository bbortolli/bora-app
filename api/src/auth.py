from flask import request
from functools import wraps
from datetime import datetime, timedelta
from jwt import encode, decode, ExpiredSignatureError
from werkzeug import security
from src.utils import res_success, res_error
from cfg.settings import SALT, SECRET

def login():
  data = request.json
  email = data.get('email')
  password = data.get('password')

  if not email or not password:
    return res_error(400, 'Required field: email and password')

  user = db.find_one('user', 'email', email)
  if not user:
    return res_error(401, 'Incorrect credentials.')

  hash_password = security.pbkdf2_hex(password, SALT, 69)
  if user.get('password') == hash_password:
    payload ={
      'exp': datetime.utcnow() + timedelta(minutes=30),
      'id': str(user.get('_id'))
    }
    encoded_jwt = encode(payload, SECRET, algorithm='HS256')
    return res_success(200, {'jwt': encoded_jwt.decode('utf-8')})

  return res_error(401, 'Incorrect credentials.')


def login_required(fn):
  @wraps(fn)
  def login_decorator(*args, **kwargs):
    auth = request.headers.get('Authorization')
    if not auth:
      return res_error(401, "Unauthorized.")
    try:
      jwt = decode(auth, SECRET, algorithms='HS256')
      return fn(*args, **kwargs)
    except ExpiredSignatureError:
      return res_error(401, "Unauthorized.")

  return login_decorator

def request_user_id(req):
  auth = req.headers.get('Authorization')
  try:
    decoded = decode(auth, SECRET, algorithms='HS256')
    return decoded.get('id')
  except:
    return None
