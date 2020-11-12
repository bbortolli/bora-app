from flask import request
from src.utils import res_success, res_error
from src.auth import login_required, request_user_id
import cfg.db as db
import re

##############################################
###       Utilities for internal use       ###
##############################################

def validate_group(group = {}):
  required_fields = ['from_location', 'to_location', 'name']
  error = []

  # Required validation
  for req in required_fields:
    field = group.get(req)
    if not field:
      error.append('Required field: ' + str(req))

  if not len(error):
    from_location = group.get('from_location')
    to_location = group.get('to_location')
    name = group.get('name')
    co_owners = group.get('co_owners')

  if len(error):
    return {
      'error': error
    }
  else:
    return {
      'data': {
        'from_location': from_location,
        'to_location': to_location,
        'name': name,
        'users': [],
        'requests': [],
        'invites': []
      }
    }

def manage_group(f, group_id, array, value):
  if f == 'add':
    updated_group = db.push_to_array_by_id('group', group_id, array, value)
  elif f == 'remove':
    updated_group = db.remove_from_array_by_id('group', group_id, array, value)
  else:
    updated_group = None

  return updated_group

def manage_user(f, user_id, array, value):
  if f == 'add':
    updated_user = db.push_to_array_by_id('user', user_id, array, value)
  elif f == 'remove':
    updated_user = db.remove_from_array_by_id('user', user_id, array, value)
  else:
    updated_group = None

  return updated_user

##############################################
###           External endpoints           ###
##############################################

@login_required
def get(id):
  id_request = request_user_id(request)
  group = db.find_by_id('group', id)

  authorized = id_request == group.get('owner_id') or id_request in group.get('users')
  if authorized:
    return res_success(200, group)
  else:
    return res_success(200)

@login_required
def insert():
  valid_group = validate_group(request.json)
  error = valid_group.get('error')
  if error:
    return res_error(400, error)

  id_request = request_user_id(request)
  data = valid_group.get('data')
  data.update(owner_id = id_request)
  new_group = db.insert('group', data)

  if not new_group:
    res_error(500, 'Error in registration.')

  updated_user = manage_user('add', id_request, 'groups', new_group)
  return res_success(200, {'id': new_group}) if updated_user else res_error(500, 'Error in registration.')

@login_required
def add_user(group_id, user_id):
  id_request = request_user_id(request)
  group = db.find_by_id('group', group_id)
  if not group:
    return res_error(400, 'Group do not exists.')

  if group.get('owner_id') != id_request:
    return res_error(401, 'Unauthorized.')

  group_users = group.get('users')
  group_requests = group.get('requests')
  group_invites = group.get('invites')

  if user_id in group_users:
    return res_success(200, 'User already a member.')

  if user_id in group_invites:
    return res_success(200, 'User already invited.')

  if user_id in group_requests:
    # adicionar no grupo
    updated_user = manage_user('add', user_id,  'groups', group_id)
    updated_group = manage_group('add', group_id, 'users', user_id)
    updated_group_2 = manage_group('remove', group_id, 'requests', user_id)
    return res_success(200, 'User accepted.')
  else:
    updated_user = manage_user('add', user_id, 'invites', group_id)
    updated_group = manage_group('add', group_id, 'invites', user_id)
    return res_success(200, 'User invited.')

@login_required
def join(group_id):
  id_request = request_user_id(request)
  group = db.find_by_id('group', group_id)
  if not group:
    return res_error(400, 'Group do not exists.')

  group_users = group.get('users')
  group_requests = group.get('requests')
  group_invites = group.get('invites')

  if id_request in group_users:
    return res_success(200, 'User already in group.')

  if id_request in group_requests:
    return res_success(200, 'Request already send.')

  if id_request in group_invites:
    updated_group = manage_group('add', group_id, 'users', id_request)
    updated_group_2 = manage_group('remove', group_id, 'invites', id_request)
    updated_user = manage_user('add', id_request, 'groups', group_id)
    updated_user_2 = manage_user('remove', id_request, 'invites', group_id)
    return res_success(200, 'Joined.')
  else:
    updated_group = manage_group('add', group_id, 'invites', id_request)
    return res_success(200, 'Request send.')
