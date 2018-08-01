from datetime import datetime
from Bookmark import Bookmark
#from couchdb.client import Server
#from couchdb.session import create_session
from couchdbkit import *


server = Server()
db = server.get_or_create_db("python_test")
Bookmark.set_db(db)

the_url=raw_input('Enter website URL: ')
the_title=raw_input('Enter website title: ')

bmark = Bookmark(
  url = the_url,
  title=the_title,
  date_added=datetime.utcnow()
)

print('Saving couchDb document')
bmark.save()
print('Document Saved!!!!')
