from common.exceptions.http.http_exception import HttpException
from common.response.http_status import HttpStatus

class UnauthorizedException(HttpException):
  def __init__(self, description='Unauthorized', payload=None):
    HttpException.__init__(
      self,
      message=description,
      payload=payload,
      status_code=HttpStatus.UNAUTHORIZED.value
    )
