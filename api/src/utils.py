from flask import Response
import json, jwt

def res_success(status, data = {}):
  data.update({
    'success': True
  })

  return Response(
    response=json.dumps(data, default=str),
    status=status,
    mimetype='application/json',
    headers={'Access-Control-Allow-Origin': '*'}
  )

def res_error(status, error = None):
  response = {
    'success': False,
    'err': error
  }

  return Response(
    response=json.dumps(response, default=str),
    status=status,
    mimetype='application/json',
    headers={'Access-Control-Allow-Origin': '*'}
  )

def dissoc(dict, *keys):
  for key in keys:
    dict.pop(key, None)
  return dict
