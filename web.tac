import os

from twisted.application import service, internet
from twisted.web import static, server

def web_app():
    file_server = server.Site(static.File(os.getcwd()));
    return internet.TCPServer(8080, file_server)

application = service.Application("Web Server")
service = web_app()
service.setServiceParent(application)
