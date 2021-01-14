from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes import routes_api
from common import setting

def bootstrap():
  port = setting.config['port-api']
  #Init server
  app = Flask(__name__)

  # Set routes
  routes_api(app)

  # Enable cors
  CORS(app)

  # Jwt manager object
  jwt = JWTManager(app)

  #Run app
  app.run(debug=True, port=port)

bootstrap()