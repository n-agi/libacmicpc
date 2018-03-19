#You do not need this two lines if you are not calling this example.
import sys
sys.path.append("..")

from _db import DB
from Parser import Parser

db = DB.instance()
p = Parser("ID", "PASSWORD")
#g contains a group
g = p.getGroup(543)
#status is a list of all status objects
status = p.getStatus(g)
for s in status:
    print s
    db.saveObject(s)
db.conn.commit()
