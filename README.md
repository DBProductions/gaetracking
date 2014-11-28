# gaetracking

To use the app engine as tracking service replace app-id in app.yaml with yours app-id.appspot.com

    <img src="http://app-id.appspot.com/?url=www.test.de" />

Additional parameter can specific the tracking data.

    <img src="http://app-id.appspot.com/?url=www.test.de&site=form&step=1" />
	
Extend the model and add more properties if more tracking data is needed.

    class Trackentry(db.Model):
        url = db.StringProperty(required=True)
        site = db.StringProperty(required=True)
        step = db.StringProperty(required=False)
        requested = db.DateTimeProperty(auto_now_add=True)

To see the tracking data use the Admin Interface or show.py as an example for a simple view.

## Feedback
Star this repo if you found it useful. Use the github issue tracker to give feedback on this repo.