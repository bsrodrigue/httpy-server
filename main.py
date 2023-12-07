import socket

from constants.http.http import HTTP_STATUS_CODE
from exceptions.http.http import HTTPError

BUFSIZE = 1024
HTTP_VERSION = "1.1"
HTTP_PROTOCOL = "HTTP/" + HTTP_VERSION

### HTTP RESPONSE FORMAT
# Response Line
# Response Header
# Response Header
# Response Header
# ... ... ... ...
# Response Header
# Blank Line
# Response Body


class HTTPResponse:
    def __init__(self, status=HTTP_STATUS_CODE.OK, body=""):
        self.status = status
        self.body = body
        self.headers = ["Server: Fagglab-Server\r\n", "Content-Type: text/html\r\n"]

    def add_header(self, key, value):
        self.headers.append(f"{key}: {value}\r\n")

    def __str__(self):
        response_line = "{0} {1}\r\n".format(HTTP_PROTOCOL, self.status.value)
        response_headers = "".join(self.headers)
        blank_line = "\r\n"
        response_body = self.body
        return "".join([response_line, response_headers, blank_line, response_body])


class HTTPRequest:
    def __init__(self, data):
        self.method = None
        self.uri = None
        self.http_version = HTTP_VERSION

        self.parse(data)

    def parse(self, data):
        lines = data.split(b"\r\n")

        request_line = lines[0]

        words = request_line.split(b" ")

        self.method = words[0].decode()

        if len(words) > 1:
            self.uri = words[1].decode()

        if len(words) > 2:
            # TODO: Determine if a certain http version should be enforced or not
            self.http_version = words[2]


class TCPServer:
    protocol = "TCP"

    def __init__(self, host="127.0.0.1", port=3000):
        self.host = host
        self.port = port

    def setup_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        return s

    def start(self):
        s = self.setup_socket()
        s.listen(5)

        print("Server listening at: ", s.getsockname())

        while True:
            conn, addr = s.accept()

            print("[{0}]Connection established with: {1}".format(self.protocol, addr))

            req_data = conn.recv(BUFSIZE)
            request = HTTPRequest(req_data)
            # TODO: Add request data processing logic for the server
            # TODO: Add logging logic for the server

            response = b""

            try:
                http_response = self.handle_request(request)
                response = http_response
            except HTTPError as e:
                http_response = HTTPResponse(e.status_code, e.message)
                response = bytes(str(http_response), "ascii")
            except Exception as e:
                http_response = HTTPResponse(
                    HTTP_STATUS_CODE.SERVER_ERROR, "A Server Error occured"
                )
                response = bytes(str(http_response), "ascii")
                print(response)
            finally:
                conn.sendall(response)
                conn.close()

    def handle_request(self, request: HTTPRequest):
        return b""


class HTTPServer(TCPServer):
    protocol = "HTTP"

    def handle_request(self, request: HTTPRequest):
        method = request.method

        if method == "GET":
            self.handle_get(request)

        elif method == "POST":
            raise NotImplemented()

        else:
            raise NotImplemented()

    def handle_get(self, request: HTTPRequest):
        raise NotImplemented()


if __name__ == "__main__":
    server = HTTPServer()
    server.start()
