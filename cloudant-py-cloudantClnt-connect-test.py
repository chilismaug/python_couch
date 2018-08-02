from datetime import datetime
from Bookmark import Bookmark

from cloudant import *

client = Cloudant("9a3f53d4-0a49-41a9-9be6-975daf80af62-bluemix", "1d1b4a88d4b37de7f5446dde59496bf1e94be13c69969f76f276cd5e6dfc604b", url = "https://9a3f53d4-0a49-41a9-9be6-975daf80af62-bluemix:1d1b4a88d4b37de7f5446dde59496bf1e94be13c69969f76f276cd5e6dfc604b@9a3f53d4-0a49-41a9-9be6-975daf80af62-bluemix.cloudant.com")
client.connect()

print ('Databases: {0}'.format(client.all_dbs()))

dbName = "python_test"
db = client[dbName]

if db.exists():
  print "'{0}' successfully found. \n".format(dbName)
