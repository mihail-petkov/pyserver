import socket

class Config:
  
  ADDRESS_FAMILY = socket.AF_INET
  SOCKET_TYPE = socket.SOCK_STREAM
  SOCKET_LEVEL = socket.SOL_SOCKET
  SOCKET_LEVEL_TYPE = socket.SO_REUSEADDR
  REQUEST_QUEUE_SIZE = 5

  def __init__(self, host, port):
    self.name = socket.getfqdn(host)
    self.host = host
    self.port = port

  @property
  def address_family(self):
    return self.ADDRESS_FAMILY

  @property
  def socket_type(self):
    return self.SOCKET_TYPE

  @property
  def socket_level(self):
    return self.SOCKET_LEVEL

  @property
  def socket_level_type(self):
    return self.SOCKET_LEVEL_TYPE

  @property
  def request_queue_size(self):
    return self.REQUEST_QUEUE_SIZE