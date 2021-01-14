from flask import jsonify
from modules.users.user_controller import Users
from modules.auth.auth_controller import Auth
from routes import handle_error

def routes_api(app):
  app.register_blueprint(Users)
  app.register_blueprint(Auth)
  handle_error(app)



