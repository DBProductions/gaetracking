import os, webapp2, jinja2
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from models import *

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
            tracklist.append({'url': i.url,'site': i.site,'step': i.step, 'requested': str(i.requested)})
        template = jinja_environment.get_template('templates/index.html')
        self.response.write(template.render({'head':'Showing ' + url,'list': tracklist}))

app = webapp2.WSGIApplication([('/show', ShowHandler)])
