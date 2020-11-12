from flask import request
from werkzeug import security
from bson.objectid import ObjectId
from src.utils import res_success, res_error
from src.auth import login_required, request_user_id
from cfg.settings import SALT
import cfg.db as db
import re

##############################################
### Basic CRUD operations for internal use ###
##############################################

def insert():
  valid_user = validate_user(request.json)
  error = valid_user.get('error')
  if error:
    return res_error(400, error)

  data = valid_user.get('data')
  exists_email = db.find_one('user', 'email', data.get('email'))
  if exists_email:
      return res_error(400, 'Email already in use.')
  exists_cpf = db.find_one('user', 'cpf', data.get('cpf'))
  if exists_cpf:
      return res_error(400, 'CPF already in use.')
  new_user = db.insert('user', data)

  return res_success(200, {'id': str(data.get('_id'))}) if new_user else res_error(500, 'Error in registration.')

def update():
  id_request = validate_login(request)
  if not id_request:
    return res_error(403, 'Please connect first.')

  if id and len(id) == 24:
    user = db.update_by_id('user', id_request, )
    if not user:
      return res_error(400, 'User do not exists.')
  return res_success(200)

##############################################
###       Utilities for internal use       ###
##############################################

def validate_user(user = {}):
  required_fields = ['email', 'password', 're_password', 'cpf']
  error = []

  # Required validation
  for req in required_fields:
    field = user.get(req)
    if not field:
      error.append('Required field: ' + str(req))

  if not len(error):
    email = user.get('email')
    password = user.get('password')
    re_password = user.get('re_password')
    cpf = user.get('cpf')

    # Type validation
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not isinstance(email, str) or not re.search(email_regex, email):
      error.append('Invalid field: email.')
    if not isinstance(password, str) or len(password) < 8:
      error.append('Invalid field: password.')
    if not isinstance(re_password, str) or len(re_password) < 8:
      error.append('Invalid field: re_password.')
    if not isinstance(cpf, str) or len(cpf) != 11:
      error.append('Invalid field: CPF.')

    # Value validation
    if password and re_password and password != re_password:
      error.append('Passwords not match.')

  if len(error):
    return {
      'error': error
    }
  else:
    return {
      'data': {
        'email': email,
        'password': security.pbkdf2_hex(password, SALT, 69),
        'cpf': cpf,
        'groups': [],
        'invites': []
      }
    }

##############################################
###           External endpoints           ###
##############################################

@login_required
def get(id):
    user_id = request_user_id(request)
    user = db.find_by_id('user', id)

    if not user:
      return res_success(200)

    if id == user_id:
      return res_success(200, user)
    else:
      data = {
        'id': str(user.get('_id')),
        'email': user.get('email')
      }
      return res_success(200, data)

@login_required
def groups(id):
  user_id = request_user_id(request)
  if user_id != id:
    return res_error(401, 'Unauthorized.')

  user = db.find_by_id('user', user_id)
  if not user:
    return res_error(400, 'User do not exists.')

  id_list = list(map(lambda id: ObjectId(id), user.get('groups')))
  groups = db.find_many('group', '_id', id_list)
  if len(groups):
    return res_success(200, groups)
  else:
    return res_error(400, 'Group do not exists.')
