from google.appengine.ext import db

class Trackentry(db.Model):
    url = db.StringProperty(required=True)
    site = db.StringProperty(required=False)
    step = db.StringProperty(required=False)
    requested = db.DateTimeProperty(auto_now_add=True)