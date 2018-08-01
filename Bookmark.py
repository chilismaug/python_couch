from couchdbkit.schema import *

class Bookmark(Document):
    url =StringProperty()
    title = StringProperty()
    date_added = DateTimeProperty()
