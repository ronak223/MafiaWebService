'''
Created on Sep 23, 2013

@author: Ronak
'''
from datetime import datetime

class Kills(object):
    '''
    Class that will denote kills
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.killerID=None
        self.victimID=None
        self.timestamp=None
        self.kill_location=[]
        
    def setKillerID(self, killerID):
        self.killerID=killerID
        
    def getKillerID(self):
        return self.killerID
    
    def setVictimID(self, victimID):
        self.victimID = victimID
        
    def getVictimID(self):
        return self.victimID
    
    def setTimestamp(self):
        self.timestamp = datetime.now()
    
    def getTimestamp(self):
        return self.timestamp
    
    def setKillLocation(self, latitude, longitude):
        self.kill_location[0] = latitude
        self.kill_location[1] = longitude
        
    def getKillLocation(self):
        return self.kill_location