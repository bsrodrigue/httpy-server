from  constants.http.http import *

class HTTPError(Exception):
    def __init__(self, message="SERVER_ERROR", status_code = HTTP_STATUS_CODE.SERVER_ERROR):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class BadRequest(HTTPError):
    def __init__(self, message="BAD_REQUEST", status_code=HTTP_STATUS_CODE.BAD_REQUEST):
        super().__init__(message, status_code)

class NotImplemented(HTTPError):
    def __init__(self, message="NOT_IMPLEMENTED", status_code=HTTP_STATUS_CODE.NOT_IMPLEMENTED):
        super().__init__(message, status_code)
