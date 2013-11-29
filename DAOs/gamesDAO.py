'''
Created on Sep 25, 2013

@author: Ronak
'''
from datetime import datetime, timedelta

from DAOs import *
from Models.games import Game


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
                      "isNight": gameObj.isNight,
                      "isActive": gameObj.isActive
                      }
        GAMES_COLLECTION.insert(cur_game)
        
    def switchDayNight(self):
        cur_game = GAMES_COLLECTION.find_one()
        if cur_game["isNight"] == True:
            GAMES_COLLECTION.update({}, {"$set": {"isNight": False}})
        else:
            GAMES_COLLECTION.update({}, {"$set": {"isNight": True}})
        return "Day/Night Switched."
    
    def getGame(self):
        cur_game_dict = GAMES_COLLECTION.find_one()
        if cur_game_dict == None:
            return None
        else:
            cur_game = {'creationTimestamp':cur_game_dict['creationTimestamp'],
                        'isNight':cur_game_dict['isNight'],
                        'dayNightFrequency': cur_game_dict['dayNightFrequency'],
                        'isActive': cur_game_dict['isActive']
                        }
            return cur_game
        
    def getGameActivity(self):
        cur_game_dict = GAMES_COLLECTION.find_one()
        if cur_game_dict == None:
            return False
        else:
            if cur_game_dict['isActive'] == True:
                return True
            else:
                return False
            
    def currentTimeState(self):
        cur_game_dict = GAMES_COLLECTION.find_one()
        if cur_game_dict == None:
            return None
        else:
            start_time = cur_game_dict['creationTimestamp']
            freq = cur_game_dict['dayNightFrequency']
            cur_time = datetime.now()
            
            datetime_elapsed = cur_time - start_time 
            hours_elapsed = datetime_elapsed.total_seconds() // 3600
            total_freqs = hours_elapsed // freq 
            if total_freqs % 2 == 0:
                return "day"
            else:
                return "night"
            
            
            
            
            
            
        
        
        
        