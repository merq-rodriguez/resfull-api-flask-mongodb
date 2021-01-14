from flask import Blueprint, request, jsonify
from modules.users import userService
from common.exceptions import InternalServerError

Users = Blueprint('users', __name__)

@Users.route('/users')
def get_users():
  response = userService.get_users()
  return jsonify(response)

@Users.route('/users/<id>')
def find_user(id):
  response = userService.find_user(id)
  return jsonify(response)

@Users.route('/users', methods=['POST'])
def create_user():
  data = request.json
  response = userService.create_user(data)
  return jsonify(response)

@Users.route('/users/<id>', methods=['PUT'])
def update_user(id):
  data = request.json
  response = userService.update_user(id, data)
  return jsonify({"message": "User updated"})

@Users.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
  response = userService.find_user(id)
  return jsonify({"message": "User deleted"})