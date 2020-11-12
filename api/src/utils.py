from flask import Response
import json, jwt

def res_success(status, data = None):
  response = {
    'success': True,
    'data': data
  }
  return Response(response=json.dumps(response, default=str), status=status, mimetype='application/json')

def res_error(status, error = None):
  response = {
    'success': False,
    'error': error
  }
  return Response(response=json.dumps(response, default=str), status=status, mimetype='application/json')
