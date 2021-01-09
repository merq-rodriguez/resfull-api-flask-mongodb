from flask import jsonify, request
from flask_restful import Resource
from common import MongoConnection
from modules.users import userService

class UserDataController(Resource):
  def get(self, id):
    user = userService.find_user(id)
    return jsonify(user)
  
  def put(self, id):
    data = request.json
    response = userService.update_user(id, data)
    return jsonify({"message": "User updated"})
  
  def delete(self, id):
    response = userService.delete_user(id)
    return jsonify({"message": "User deleted"})