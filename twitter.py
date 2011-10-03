from ConfigParser import ConfigParser
from urllib2 import urlopen
import json
import cyclone

config = ConfigParser()
config.read(["site.conf"])

class TwitterHandler(cyclone.web.RequestHandler):
	def get(self):
		out = "<ul>%s</ul>"
		tw_data = json.loads(urlopen("http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s" % config.get("twitter", "username")).read())
		data = ""
		for tw in tw_data[:-10]:
			if tw["in_reply_to_screen_name"] == None:
				data += "<li>%s</li>\n" % tw["text"]
		self.write(out % data)