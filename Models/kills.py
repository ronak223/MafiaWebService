'''
Created on Sep 23, 2013

@author: Ronak
'''
from datetime import datetime

class Kill(object):
    '''
    Class that will denote kills
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.location = []
        self.killerID=""
        self.victimID=""
        self.timestamp=""
        
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
    
    def setLocation(self, latitude, longitude):
        self.location.append(latitude)
        self.location.append(longitude)
        
    def getLocation(self):
        return self.location