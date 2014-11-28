import os, webapp2, jinja2
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from models import *

class TrackHandler(webapp2.RequestHandler):
    def get(self):
        url = self.request.get('url')
        site = self.request.get('site')
        step = self.request.get('step')
        if url:
            t = Trackentry(url = url, site = site, step = step)
            t.put()
        self.response.headers["Content-Type"] = "image/gif"
        self.response.write('')

app = webapp2.WSGIApplication([('/', TrackHandler)])
