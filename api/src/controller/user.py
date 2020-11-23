from flask import request
from werkzeug import security
from bson.objectid import ObjectId
from mongoengine.queryset.visitor import Q
from src.utils import res_success, res_error, dissoc
from src.auth import login_required, request_user_id
from src.model.User import User
from cfg.settings import SALT
import datetime
import re

##############################################
### Basic CRUD operations for internal use ###
##############################################

def insert():
  data = request.json
  email = data.get('email')
  document = data.get('document')
  password = data.get('password')
  re_password = data.get('re_password')

  if password and re_password and password != re_password:
    return res_error(200, 'Password and verification required.')

  try:
    User.objects.get(Q(email = email) | Q(document = document))
    return res_error(200, 'Email or document already in use.')
  except User.DoesNotExist:
    pass

  try:
    data.update(
      friends = [],
      groups = [],
      events = [],
      invites = [],
      password = security.pbkdf2_hex(password, SALT, 69),
      created_at = datetime.datetime.utcnow
    )
    user = User(**dissoc(data, 're_password'))
    user.validate()
    created = user.save().to_mongo().to_dict()
    return res_success(200, {'id': created['_id']})
  except Exception as e:
    print(e)
    return res_error(400, e)

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



##############################################
###           External endpoints           ###
##############################################

@login_required
def get(id):
    user_id = request_user_id(request)
    user = User.objects(_id = user_id)

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
