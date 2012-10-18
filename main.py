import webapp2
from google.appengine.ext import db

class Trackentry(db.Model):
    url = db.StringProperty(required=True)
    site = db.StringProperty(required=True)
    requested = db.DateTimeProperty(auto_now_add=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        url = self.request.get('url')
        site = self.request.get('site')
        if site and url:
            t = Trackentry(url = url, site = site)
            t.put()
        self.response.headers["Content-Type"] = "image/gif"

app = webapp2.WSGIApplication([('/', MainHandler)])
