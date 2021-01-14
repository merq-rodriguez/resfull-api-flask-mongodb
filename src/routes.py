from flask import jsonify
from modules.users.user_controller import Users
from common.exceptions import NotFoundException, InternalServerError

def routes_api(app):
  app.register_blueprint(Users)

  @app.errorhandler(NotFoundException)
  def not_found_exception(e):
    return jsonify(e.response), e.status_code

  @app.errorhandler(InternalServerError)
  def resource_not_found(e):
    return jsonify(e.response), e.status_code

