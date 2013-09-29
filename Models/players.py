'''
Created on Sep 23, 2013

@author: Ronak
'''

class Player(object):
    '''
    Represents players that are actually under the username.
    '''

    def __init__(self):
        self.userID=None
        self.alignment=None
        self.isDead = False
        #to show who has player has voted to kill
        self.votedAgainst=""
        self.location=[]
        self.isAdmin = False
        
    def isWerewolf(self):
        if(self.alignment=="Werewolf"):
            return True
        else:
            return False
        
    def setAlignment(self, alignment):
        self.alignment = alignment
        
    def getAlignment(self):
        return self.alignment
        
    def getUserID(self):
        return self.userID
    
    def setUserID(self, playerID):
        self.userID = playerID
    
    def isDead(self):
        return self.isDead
    
    def setDead(self):
        self.isDead = True
    
    def getVotedAgainst(self):
        return self.votedAgainst
    
    def setVotedAgainst(self, voted_against):
        self.votedAgainst = voted_against  
        
    def getLatitude(self):
        return self.location[0]
    
    def getLongitude(self):
        return self.location[1]
    
    def getLocation(self):
        return self.location
    
    def setLocation(self, latitude, longitude):
        #self.location.append(latitude)
        #self.location.append(longitude)
        self.location= [latitude, longitude]
        
    def isAdmin(self):
        return self.isAdmin
    
    def makeAdmin(self):
        self.isAdmin = True
    
    
           
        