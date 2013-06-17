import os, webapp2, jinja2
from google.appengine.ext import db
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Trackentry(db.Model):
    url = db.StringProperty(required=True)
    site = db.StringProperty(required=True)
    step = db.StringProperty(required=False)
    requested = db.DateTimeProperty(auto_now_add=True)

class TrackHandler(webapp2.RequestHandler):
    def get(self):
        url = self.request.get('url')
        site = self.request.get('site')
        step = self.request.get('step')
        if site and url:
            t = Trackentry(url = url, site = site, step = step)
            t.put()
        self.response.headers["Content-Type"] = "image/gif"
        self.response.write('')

class ShowHandler(webapp2.RequestHandler):
    def get(self):
        url = self.request.get('url')
        if url:
            t = Trackentry.gql("WHERE url = :1", url)
        else:
            t = Trackentry.all()
            url = 'all'
        track = t.fetch(20)
        tracklist = []
        for i in track:
            tracklist.append({'url': i.url,'site': i.site, 'requested': str(i.requested)})
        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render({'head':'Showing ' + url,'list': tracklist}))

app = webapp2.WSGIApplication([('/', TrackHandler),('/show', ShowHandler)])
