from flask import jsonify
from common.exceptions import NotFoundException, InternalServerError, BadRequestException, UnauthorizedException

def handle_error(app):
  @app.errorhandler(NotFoundException)
  def not_found_exception(e):
    return jsonify(e.response), e.status_code

  @app.errorhandler(InternalServerError)
  def internal_server_error(e):
    return jsonify(e.response), e.status_code

  @app.errorhandler(UnauthorizedException)
  def unauthorized(e):
    return jsonify(e.response), e.status_code

  @app.errorhandler(BadRequestException)
  def bad_request_exception(e):
    return jsonify(e.response), e.status_code