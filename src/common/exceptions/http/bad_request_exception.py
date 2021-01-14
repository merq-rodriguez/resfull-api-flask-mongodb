
from common.exceptions.http.http_exception import HttpException
from common.response.http_status import HttpStatus

class BadRequestException(HttpException):

  def __init__(self, description='Bad Request', payload=None ):
    HttpException.__init__(
      self,
      message=description,
      payload=payload,
      status_code=HttpStatus.BAD_REQUEST.value
    )