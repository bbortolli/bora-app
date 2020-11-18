from flask import Response
import json, jwt

def res_success(status, data = {}):
  data.update({
    'success': True
  })
  return Response(response=json.dumps(data, default=str), status=status, mimetype='application/json')

def res_error(status, error = None):
  response = {
    'success': False,
    'err': error
  }
  return Response(response=json.dumps(response, default=str), status=status, mimetype='application/json')
