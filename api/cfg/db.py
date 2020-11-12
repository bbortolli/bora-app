from src import db_session as db
from bson.objectid import ObjectId

def find_all(coll):
  try:
    coll = db[coll]
    data = coll.find({})
    return list(data)
  except:
    return None

def find_one(coll, key, value):
  try:
    coll = db[coll]
    data = coll.find_one({key: value})
    return data
  except:
    return None

def find_many(coll, key, values):
  try:
    coll = db[coll]
    query = {key: {'$in': values}}
    result = list(coll.find(query))
    return result
  except:
    return None

def find_by_id(coll, id):
  return find_one(coll, '_id', ObjectId(id))

def insert(coll, data):
  try:
    coll = db[coll]
    new_data = coll.insert_one(data)
    return str(new_data.inserted_id)
  except:
    return None

def update_by_id(coll, id, value):
  try:
    new_value = value.update(_id = ObjectId(id))
    coll = db[coll]
    new_data = coll.save(new_value)
    return new_data
  except:
    return None

def push_to_array_by_id(coll, id, array, value):
  try:
    query = {'$push': {array: value}}
    coll = db[coll]
    new_data = coll.update({'_id': ObjectId(id)}, query)
    return new_data
  except:
    return None

def remove_from_array_by_id(coll, id, array, value):
  try:
    query = {'$pull': {array: value}}
    coll = db[coll]
    new_data = coll.update({'_id': ObjectId(id)}, query)
    return new_data
  except:
    return None
