
from common.exceptions.http.http_exception import HttpException
from common.response.http_status import HttpStatus

class NotFoundException(HttpException):

  def __init__(self, description='Not Found', payload=None ):
    HttpException.__init__(
      self,
      message=description,
      payload=payload,
      status_code=HttpStatus.NOT_FOUND.value
    )