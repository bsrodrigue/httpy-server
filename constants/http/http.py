from enum import Enum

class HTTP_STATUS_CODE(Enum):
    """
    Enumeration of commonly used HTTP status codes. 
    """
    OK = 200  # Standard response for successful HTTP requests.
    CREATED = 201  # The request has been fulfilled, and a new resource is created.
    ACCEPTED = 202  # The request has been accepted for processing, but the processing has not been completed.
    NO_CONTENT = 204  # The server successfully processed the request, but there is no content to send.

    BAD_REQUEST = 400  # The server could not understand the request due to invalid syntax or missing request parameters.
    UNAUTHORIZED = 401  # The client must authenticate itself to get the requested response.
    FORBIDDEN = 403  # The client does not have permission to access the requested resource.
    NOT_FOUND = 404  # The server cannot find the requested resource.

    SERVER_ERROR = 500  # A generic error message returned when an unexpected condition was encountered by the server.
    NOT_IMPLEMENTED = 501  # The server either does not recognize the request method or lacks the ability to fulfill it.
    SERVICE_UNAVAILABLE = 503  # The server is not ready to handle the request. Common causes include maintenance or overload.
