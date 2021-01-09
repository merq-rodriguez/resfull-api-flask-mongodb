from common import MongoConnection
from bson import ObjectId

class UserService:

  def __init__(self):
    conn = MongoConnection()
    self._mongo = conn.db
    self._collection = self._mongo["users"]

  def find_user(self, id):
    query = { "_id": ObjectId(id) }
    user = self._collection.find_one(query)
    if not user:
      return { "message": "User not found"}
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
    user = { "name": data['name'], "password": data['password'], "email": data['email'] }
    item =  self._collection.insert_one(user)
    return {
      "id": str(ObjectId(item.inserted_id)),
      "name": data['name'],
      "password": data['password'],
      "email": data['email']
    }
  
  def update_user(self, id, data):
    user = { "name": data['name'], "password": data['password'], "email": data['email'] }
    query = { '_id': ObjectId(id) }
    item = self._collection.update_one(query,
      { 
        "$set": {
        "name": data['name'],
        "password": data['password'],
        "email": data['email']
      }
    })
    print(item)

  def delete_user(self, id):
    query = {'_id': ObjectId(id)}
    self._collection.delete_one(query)
