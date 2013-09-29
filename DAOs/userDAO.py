'''
Created on Sep 25, 2013

@author: Ronak
'''
from DAOs import *
from Models.user import User
from Crypto.Hash import MD5

class UserDAO(object):
    '''
    Allows pushing and pulling of user data to and from DB
    '''


    def __init__(self):
        '''
        Constructor
        '''
         
    def getUser(self, user):
        USERS_COLLECTION.find_one({"username": "Ronak"})
        
    def registerUser(self, userID, password):
        for user in USERS_COLLECTION.find():
            if user["userID"] == userID:
                return "Username already exists, try another."
            
        new_user = User()
        new_user.setUserID(userID)
        new_user.setPassword(password)
        cur_user = {"userID": new_user.getUserID(),
                "password": new_user.getHashedPassword(),
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
            
            
        
        
        
    
        
        