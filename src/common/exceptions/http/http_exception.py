class HttpException(Exception):
  def __init__(self, message, status_code=None, payload=None):
    super().__init__()
    self.message = message
    if status_code is not None:
        self.status_code = status_code
    self.payload = payload
    self.response = self.init_response()

  def init_response(self):
    res = {}
    if self.payload != None:
      res['error'] = dict(self.payload or ())
    res['message'] = self.message
    res['statusCode'] = self.status_code
    return res

