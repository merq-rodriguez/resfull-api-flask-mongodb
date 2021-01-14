from common import MongoConnection
from common.exceptions import UnauthorizedException
from bson import ObjectId
import bcrypt

class AuthService:
  def __init__(self):
    conn = MongoConnection()
    self._mongo = conn.db
    self._collection = self._mongo["users"]

  def signin(self, data):
    query = { "email":  data['email'] }
    user = self._collection.find_one(query)
    if not user:
      raise UnauthorizedException()
    return user