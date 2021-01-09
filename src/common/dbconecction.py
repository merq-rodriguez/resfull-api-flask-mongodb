#from flask_pymongo import PyMongo
from pymongo import MongoClient
from common.setting import Setting

class MongoConnection(object):
  __instance = None

  def __init__(self):
    setting = Setting()
    dbname      = setting.config['database']['name']
    uri_mongodb = setting.config['database']['uri-mongodb']
    self._mongo = MongoClient(uri_mongodb)
    self._db    = self._mongo[dbname]

  def __str__(self):
    return MongoConnection.__str__

  def __new__(cls):
    if MongoConnection.__instance is None:
      MongoConnection.__instance = object.__new__(cls)
    return MongoConnection.__instance

  def get_db(self):
    return self._db

  db = property(get_db)