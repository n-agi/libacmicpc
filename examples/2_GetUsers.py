#You do not need this two lines if you are not calling this example.
import sys
sys.path.append("..")

from _db import DB
from Parser import Parser

db = DB.instance()
p = Parser("ID", "PASSWORD")
# getGroupUsers returns a list contained with string of all group members
for username in p.getGroupUsers(p.getGroup(543)):
    # parser's getUser will fetch detail profile of user.
    u = p.getUser(username)
    print u
    db.saveObject(u)

#Commit your database.
db.conn.commit()
