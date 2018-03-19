import sqlite3
from Model import *
from base import BOJObject
class SingletonInstance:
    __instance = None
    @classmethod
    def __getInstance(cls):
        return cls.__instance
    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
	cls.instance = cls.__getInstance
	return cls.__instance

class NoGroupFoundException(Exception):
    pass
class NoExerciseFoundException(Exception):
    pass
class NoUserFoundException(Exception):
    pass

class DB(SingletonInstance):
    def __init__(self):
        import os
        self.path = os.path.realpath(os.path.dirname(__file__)) + "/acmicpc.db"
        print self.path
        self.conn = sqlite3.connect(self.path, check_same_thread=False)
        self.cursor= self.conn.cursor()
        self.initDB()
    def initDB(self):
        for c in BOJObject.__subclasses__():
            self.cursor.execute(c.to_sql())
        self.conn.commit()
    def saveObject(self, obj):
        query = obj.to_sql2()
        values = []
        for s in obj.__slots__:
            values.append(obj.__getattribute__(s))
        self.cursor.execute(query, values)
