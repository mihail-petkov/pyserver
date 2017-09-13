class Response:

    HTTP_VERSION = 'HTTP/1.1'

    def __init__(self, status, headers, body):
        self.status = status
        self.headers = headers
        self.body = body

    def get(self):
        response = '{http_version} {status}\r\n'.format(http_version=self.HTTP_VERSION, status=self.status)
        for header in self.headers:
            response += '{0}: {1}\r\n'.format(*header)
        response += '\r\n'
        for data in self.body:
            response += data
        print(response)
        return response.encode('utf-8')
