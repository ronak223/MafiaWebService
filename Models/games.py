'''
Created on Sep 23, 2013

@author: Ronak
'''
from datetime import datetime

class Game(object):
    '''
    For controlling overarching games.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.creationTime = datetime.now()
        self.dayNightFrequency = 24
        
    def getStartTimestamp(self):
        return self.creationTime
    
    def setFrequency(self, freq):
        self.dayNightFrequency = freq
        
    def getFrequency(self):
        return self.dayNightFrequency