'''
Created on Sep 23, 2013

@author: Ronak
'''

class Player(object):
    '''
    Represents players that are actually under the username.
    '''
    #image

    def __init__(self):
        self.playerID=None
        self.alignment=None
        self.isDead=False
        #to show who has player has voted to kill
        self.votedAgainst=None
        self.location=[]
        
    def isWerewolf(self):
        if(self.alignment=="Werewolf"):
            return True
        else:
            return False
        
    def getPlayerID(self):
        return self.playerID
    
    def setPlayerID(self, playerID):
        self.playerID = playerID
    
    def isDead(self):
        return self.isDead
    
    def setDead(self):
        self.isDead = True
        
    def setLatitude(self, latitude):
        self.location[0] = latitude
    
    def setLongitude(self, longitude):
        self.location[1] = longitude
        
    def getLatitude(self):
        return self.location[0]
    
    def getLongitude(self):
        return self.location[1]
    
    def getLocation(self):
        return self.location
    
    def setLocation(self, latitude, longitude):
        self.location[0] = latitude
        self.location[1] = longitude
    
    
           
        