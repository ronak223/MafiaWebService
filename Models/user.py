'''
Created on Sep 20, 2013

@author: Ronak

'''

from Crypto.Hash import MD5

class User(object):
    '''
    Stores individual user details
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.userID = None
        self.hashedPassword = None
        self.loggedIn = False
        
    def setPassword(self, password):
        #saving hashed password
        hashed = MD5.new(password).hexdigest()
        self.hashedPassword = hashed
        
    def setUserID(self, username):
        self.userID = username
        
    def getUserID(self):
        return self.userID
    
    def getHashedPassword(self):
        return self.hashedPassword
    
    def isLoggedIn(self):
        return self.loggedIn
        
        