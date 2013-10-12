'''
Created on Sep 25, 2013

@author: Ronak
'''

from DAOs import *
from DAOs.gamesDAO import GameDAO
from DAOs.killsDAO import KillDAO
from DAOs.playersDAO import PlayerDAO
from Models.games import Game
from Models.kills import Kill


#globally accessible DAOs
playerDAO = PlayerDAO()
gamesDAO = GameDAO()
killDAO = KillDAO()

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
    if GAMES_COLLECTION.count() == 1:
        return False
    else:
        new_game = Game()
        new_game.setFrequency(freq)
        
        gamesDAO.createGame(new_game)
        
        playerDAO.updatePlayer(userID, "isAdmin", True)
        return True
    
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

def getAllAlivePlayers():
    alive_players_list = []
    for player in PLAYERS_COLLECTION.find():
        if player["isDead"] == False:
            alive_players_list.append(player)
    return alive_players_list
    
def getVotablePlayers():
    votable_players_list = getAllAlivePlayers()
    return votable_players_list

#places vote if voter is a Townsperson
def placeVote(voter_userID, votee_userID):
    cur_player = playerDAO.getPlayer(voter_userID)
    if cur_player["alignment"] == "Townsperson":
        playerDAO.updatePlayer(voter_userID, "votedAgainst", votee_userID)
        return True
    else:
        return False

#TODO: killPlayer can only be done if killer is werewolf and game state is night!
def killPlayer(killer_userID, victim_userID):
    killer = playerDAO.getPlayer(killer_userID)
    game = gamesDAO.getGame()
    if killer["alignment"] == "Werewolf":
        #getting location data for kill
        killer_loc = getCurrentLocation(killer_userID)
        
        cur_kill = Kill()
        cur_kill.setKillerID(killer_userID)
        cur_kill.setVictimID(victim_userID)
        cur_kill.setTimestamp()
        cur_kill.setLocation(killer_loc[0], killer_loc[1])
        
        killDAO.registerKill(cur_kill)
        
        #updating victim to dead
        playerDAO.updatePlayer(victim_userID, "isDead", True)
        test_conf = playerDAO.increasePlayerPoints(killer_userID, 10)
        return True
    else:
        return False
    
#returns current location in a list. Format: [latitude, longitude]    
def getCurrentLocation(userID):
    cur_player = playerDAO.getPlayer(userID)
    cur_location = cur_player["location_2d"]
    return cur_location

#returns player with highest score
def getHighscorePlayer():
    cur_highscore_player = PLAYERS_COLLECTION.find_one()
    
    for player in PLAYERS_COLLECTION.find():
        if player["points"] > cur_highscore_player["points"]:
            cur_highscore_player = player
            
    return cur_highscore_player

def wipeDatabase():
    #FOR TESTING PURPOSES ONLY!!!! Not linked to any URL; must be manually configured
    GAMES_COLLECTION.remove()
    PLAYERS_COLLECTION.remove()
    USERS_COLLECTION.remove()
    KILLS_COLLECTION.remove()

