from common import MongoConnection, HttpStatus
from common.exceptions import NotFoundException
from bson import ObjectId
from modules.security.hash_password import hash_password

class UserService:

  def __init__(self):
    conn = MongoConnection()
    self._mongo = conn.db
    self._collection = self._mongo["users"]

  def find_user(self, id):
    query = { "_id": ObjectId(id) }
    user = self._collection.find_one(query)
    if not user:
      raise NotFoundException("User not found")
    else:
      return {
        "_id": str(ObjectId(user['_id'])),
        "name": user['name'],
        "email": user['email'],
        "password": user['password']
      }

  def get_users(self):
    users = []
    for user in self._collection.find():
      users.append({
        '_id': str(ObjectId(user['_id'])),
        'name': user['name'],
        'email': user['email'],
        'password': user['password']
      })
    return users

  def create_user(self, data):
    password = hash_password(data['password'])
    user = { "name": data['name'], "password": password, "email": data['email'] }
    item =  self._collection.insert_one(user)
    return {
      "id": str(ObjectId(item.inserted_id)),
      "name": user['name'],
      "password": user['password'],
      "email": user['email']
    }

  def update_user(self, id, data):
    password = hash_password(data['password'])
    user = { "name": data['name'], "password": password, "email": data['email'] }
    query = { '_id': ObjectId(id) }
    item = self._collection.update_one(query,
      {
        "$set": {
        "name": user['name'],
        "password": user['password'],
        "email": user['email']
      }
    })

  def delete_user(self, id):
    query = {'_id': ObjectId(id)}
    self._collection.delete_one(query)
