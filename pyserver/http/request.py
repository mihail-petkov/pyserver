class Request:

    def __init__(self, request):
        self.request = request
        self.__parse_request()

    def __parse_request(self):
        info = self.request.splitlines()[0].decode('UTF-8')
        self.method, self.path, self.http_version = info.split()