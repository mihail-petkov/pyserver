import sys
import imp
from pyserver import WSGIPyServer

def validate_params():
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')

def load_application():
    app_details = sys.argv[1]
    module_path, module, app_handler = app_details.split(':')
    app_module = imp.load_source(module, module_path)
    app_handler = getattr(app_module, app_handler)
    return app_handler

def create_server():
    validate_params()
    application = load_application()
    run(application)

def run(application):
    pyserver = WSGIPyServer(application)
    pyserver.run()

if __name__ == '__main__':
    create_server()