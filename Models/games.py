'''
Created on Sep 23, 2013

@author: Ronak
'''
from datetime import datetime

class Game(object):
    '''
    For settings parameters of current game.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.creationTimestamp = datetime.now()
        self.dayNightFrequency = 24
        
    def getStartTimestamp(self):
        return self.creationTimestamp
    
    def setFrequency(self, freq):
        self.dayNightFrequency = freq
        
    def getFrequency(self):
        return self.dayNightFrequency