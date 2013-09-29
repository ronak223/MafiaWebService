'''
Created on Sep 25, 2013

@author: Ronak
'''
from DAOs import *

class GameDAO(object):
    '''
    manages game parameters in DB
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def createGame(self, gameObj):
        cur_game = {"creationTimestamp": gameObj.getStartTimestamp(),
                      "dayNightFrequency": gameObj.getFrequency(),
                      }
        GAMES_COLLECTION.insert(cur_game)
        
    def restartGame(self, userID, new_freq):
        #TODO: Remove all players and kill, and reset according to given frequency, only if current user is admin
        return
        
        