'''
Created on Sep 25, 2013

@author: Ronak
'''
from DAOs import *
from Crypto.Hash import MD5

class UserDAO(object):
    '''
    Allows pushing and pulling of user data to and from DB
    '''


    def __init__(self):
        #self.username = None
        #self.hashedPassword = None
        '''
        Constructor
        '''
         
    def getUser(self, user):
        USERS_COLLECTION.find_one({"username": "Ronak"})
        
    def registerUser(self, user):
        cur_user = {"userID": user.getUserID(),
                "password": user.getHashedPassword(),
                "loggedIn": False
                }
        USERS_COLLECTION.insert(cur_user)
        return "Player registered"
        
    def loginUser(self, userID, password):
        cur_user = USERS_COLLECTION.find_one({"userID": userID})
        if(MD5.new(password).hexdigest() == cur_user["password"]):
            USERS_COLLECTION.update({"userID": userID}, {"$set": {"loggedIn":True}})
            return True
        else:
            return False
    
    def logoutUser(self, userID):
        cur_user = USERS_COLLECTION.find_one({"userID": userID})
        if(cur_user["loggedIn"] == True):
            USERS_COLLECTION.update({"userID": userID}, {"$set": {"loggedIn":False}})
            return True
        
    def isLoggedIn(self, userID):
        cur_user = USERS_COLLECTION.find_one({"userID": userID})
        if(cur_user["loggedIn"] == True):
            return True
        else:
            return False
            
            
        
        
        
    
        
        