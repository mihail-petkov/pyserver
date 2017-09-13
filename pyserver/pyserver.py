import socket
import sys
import logging
import http.header as header        
from io import StringIO
from http.request import Request
from http.response import Response
from config import Config

class WSGIPyServer:
    
    def __init__(self, application, port=8888, host='', log_level=logging.DEBUG):
        self.application = application
        self.config = Config(host, port)
        self.log_level = log_level

    def listen(self):
        self.server = socket.socket(self.config.address_family, self.config.socket_type)
        self.server.setsockopt(self.config.socket_level, self.config.socket_level_type, 1)
        self.server.bind((self.config.host, self.config.port))
        self.server.listen(self.config.request_queue_size)
        while True:
            self.handle_request()

    def handle_request(self):
        self.connection, client_address = self.server.accept()
        self.process_request()

    def process_request(self):
        self.parse_request()
        self.process_response()

    def parse_request(self):
        request_data = self.connection.recv(1024)
        self.request = Request(request_data)

    def process_response(self):
        env = self.get_environ()
        result = self.application(env, self.start_response)
        self.finish_response(result)

    def start_response(self, status, response_headers):
        self.status = status
        self.headers = response_headers + header.get_server_headers()

    def finish_response(self, response_body):
        response = self.get_response(response_body)
        self.connection.sendall(response)
        self.connection.close()

    def get_response(self, response_body):
        response = Response(self.status, self.headers, response_body)
        return response.get()

    def get_environ(self):
        env = {}
        env['wsgi.version'] = (1, 0)
        env['wsgi.url_scheme'] = 'http'
        env['wsgi.input'] = StringIO(str(self.request))
        env['wsgi.errors'] = sys.stderr
        env['wsgi.multithread'] = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once'] = False
        env['REQUEST_METHOD'] = self.request.method
        env['PATH_INFO'] = self.request.path
        env['SERVER_NAME'] = self.config.name
        env['SERVER_PORT'] = str(self.config.port)
        return env