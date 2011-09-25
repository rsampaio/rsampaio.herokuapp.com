import os

import cyclone.web
from twisted.application import service, internet
from twisted.web import static, server

_port = int(os.environ["PORT"])

class IndexHandler(cyclone.web.RequestHandler):
    def get(self):
        self.redirect("/static/index.html")

class Application(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
        ]

        settings = {
            "static_path": "./html",
        }

        cyclone.web.Application.__init__(self, handlers, **settings)

site = Application()
application = service.Application("Web Server")
internet.TCPServer(_port, site).setServiceParent(application)
