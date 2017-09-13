from email.utils import formatdate

def get_server_headers():
    return [
        ('Date', get_header_date()),
        ('Server', 'WSGIPyServer 0.1'),
    ]

def get_header_date():
    return formatdate(timeval=None, localtime=False, usegmt=True)