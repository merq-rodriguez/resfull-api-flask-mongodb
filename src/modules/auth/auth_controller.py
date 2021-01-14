from flask import Blueprint, request, jsonify
from modules.auth import authService

Auth = Blueprint("auth", __name__)

@Auth.route('/auth/signin', methods=['POST'])
def signIn():
  data = request.json
  response = authService.signin(data)
  return jsonify(response)
