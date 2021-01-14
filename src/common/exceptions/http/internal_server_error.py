from common.exceptions.http.http_exception import HttpException
from common.response.http_status import HttpStatus

class InternalServerError(HttpException):
  def __init__(self, description='Internal Server Error', payload=None):
    HttpException.__init__(
      self,
      message=description,
      payload=payload,
      status_code=HttpStatus.INTERNAL_SERVER_ERROR.value
    )
