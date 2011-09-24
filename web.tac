import os

from twisted.application import service, internet
from twisted.web import static, server

_port = int(os.environ["PORT"])

def web_app():
    file_server = server.Site(static.File(os.path.join(os.getcwd(), "html")));
    return internet.TCPServer(_port, file_server)

application = service.Application("Web Server")
service = web_app()
service.setServiceParent(application)
