'''
Created on Sep 25, 2013

@author: Ronak
'''

from DAOs import *
from DAOs.playersDAO import PlayerDAO
from DAOs.gamesDAO import GameDAO
from Models.games import Game


#globally accessible DAOs
playerDAO = PlayerDAO()
gamesDAO = GameDAO()

def playersNearTo(userID, radius):
    cur_player = playerDAO.getPlayer(userID)
    #if cur_player.isWerewolf():
    if cur_player["alignment"] == "Werewolf":
        nearbyPlayersList = playerDAO.checkNearbyPlayersTo(userID, radius)
        aug_list = [player for player in nearbyPlayersList if player["userID"] != userID]
        return aug_list
    else:
        return False
    
def startGame(userID, freq):
    new_game = Game()
    new_game.setFrequency(freq)
    
    gamesDAO.createGame(new_game)
    
    playerDAO.updatePlayer(userID, "isAdmin", True)
    
    #PLAYERS_COLLECTION.update({"userID": userID}, {"$set": {"isAdmin":True}})
    

#restarting game with current config, if user is admin    
def restartGame(userID, new_freq):
    cur_player = playerDAO.getPlayer(userID)
    if cur_player["isAdmin"] == True:
        GAMES_COLLECTION.remove()
        KILLS_COLLECTION.remove()
        PLAYERS_COLLECTION.update({}, {"$set": {"votedAgainst":""}}, upsert=False, multi=True)
        PLAYERS_COLLECTION.update({}, {"$set": {"isDead":False}}, upsert=False, multi=True)
        startGame(userID, new_freq)
        return True
    else:
        #means that player that initiated restart was NOT admin
        return False

        
        
        
''' TESTING    
def testingGetPlayer(userID):
    cur_player = playerDAO.getPlayer(userID)
    return cur_player["userID"]
'''   