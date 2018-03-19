#You do not need this two lines if you are not calling this example.
import sys
sys.path.append("..")

from _db import DB
from Parser import Parser


db = DB.instance()
p = Parser("[ACMICPC USERNAME HERE]", "[ACMICPC PASSWORD HERE]")

#Parser goes on web and fetches, make Group Object
group = p.getGroup(543)

#If you need to use sqlite3 cache, feel free to use.
print db.saveObject(group)
#Don't forget to commit.
db.conn.commit()

