'''
Created on Sep 20, 2013

@author: Ronak
'''

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

        