from flask import jsonify, request
from flask_restful import Resource
from common import MongoConnection
from modules.users import userService

class UserController(Resource):
  def get(self):
      users = userService.get_users()
      return jsonify(users)

  def post(self):
    data = request.json
    response = userService.create_user(data)
    return jsonify(response)