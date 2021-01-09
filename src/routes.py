from flask_restful import Api
from modules.users.controllers.user_controller import UserController
from modules.users.controllers.user_data_controller import UserDataController

def routes_api(app):
  api = Api(app)
  api.add_resource(UserController, '/users')
  api.add_resource(UserDataController, '/users/<id>')
