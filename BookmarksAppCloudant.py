from datetime import datetime
from Bookmark import Bookmark
#from couchdb.client import Server
#from couchdb.session import create_session
from cloudant.client import Cloudant
from cloudant.document import Document

client = Cloudant("9a3f53d4-0a49-41a9-9be6-975daf80af62-bluemix", "1d1b4a88d4b37de7f5446dde59496bf1e94be13c69969f76f276cd5e6dfc604b", url = "https://9a3f53d4-0a49-41a9-9be6-975daf80af62-bluemix:1d1b4a88d4b37de7f5446dde59496bf1e94be13c69969f76f276cd5e6dfc604b@9a3f53d4-0a49-41a9-9be6-975daf80af62-bluemix.cloudant.com")
client.connect()

dbName = "python_test"
db = client[dbName]

#server = Server()
#db = server.get_or_create_db(dbName)
print ('Databases: {0}'.format(client.all_dbs))

if db.exists():
  print "'{0}' successfully found. \n".format(dbName)
else:
    db = client.create_database(dbName)
    print "'{0}' successfully created. \n".format(dbName)

print('We think we have Deeeeb! Now bind Bookmark class to it...')
Bookmark.set_db(db)

the_url=raw_input('Enter website URL: ')
the_title=raw_input('Enter website title: ')

#bmark = Bookmark(
#  url = the_url,
#  title=the_title,
#  date_added=datetime.utcnow()
#)

print('Saving couchDb document')
with Document(db, the_url) as document:
    document['url'] = the_url
    document['title'] = the_title
    document['date_added'] = datetime.utcnow().isoformat()
print('Document Saved!!!!')
