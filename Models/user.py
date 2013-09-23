'''
Created on Sep 20, 2013

@author: Ronak

'''
from urlparse import urlparse
import os
import pymongo

MONGO_URL = os.environ.get('MONGOHQ_URL')
#MONGO_URL = os.environ.get('MONGOHQ_URL')
#client = MongoClient(MONGO_URL);
# Specify the database
#db = client.app18266596
#user_collection = db.users
db=None

if MONGO_URL:
    # Get a connection
    conn = pymongo.Connection(MONGO_URL)
    
    # Get the database
    db = conn[urlparse(MONGO_URL).path[1:]]
    user_collection = db.users

class User(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.username = None
        self.hashedPassword = None
        
    def setPassword(self, password):
        #TODO: Needs hash function
        self.hashedPassword = password
        
    def setUsername(self, username):
        self.username = username
        
    def getUsername(self):
        return self.username
    
    def getHashedPassword(self):
        return self.hashedPassword
    def sendToDb(self):
        cur_user = {"name": self.username,
                    "password": self.password
                    }
        cur_user_id = user_collection.insert(cur_user)
        
        