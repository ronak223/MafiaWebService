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
        self.isNight = False
        
    def getStartTimestamp(self):
        return self.creationTimestamp
    
    def setFrequency(self, freq):
        self.dayNightFrequency = freq
        
    def getFrequency(self):
        return self.dayNightFrequency
    
    def setDay(self):
        self.isNight = False
        
    def setNight(self):
        self.isNight = True
        
    def isNight(self):
        return self.isNight