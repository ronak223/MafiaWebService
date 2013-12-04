'''
Created on Sep 25, 2013

@author: Ronak
'''

from Crypto.Random.random import randrange

from DAOs import *
from DAOs.gamesDAO import GameDAO
from DAOs.killsDAO import KillDAO
from DAOs.playersDAO import PlayerDAO
from Models.games import Game
from Models.kills import Kill
from Models.players import Player


#globally accessible DAOs
playerDAO = PlayerDAO()
gamesDAO = GameDAO()
killDAO = KillDAO()

def playersNearTo(userID, radius):
    cur_player = playerDAO.getPlayer(userID)
    #if cur_player.isWerewolf():
    if cur_player["alignment"] == "Werewolf":
        nearbyPlayersList = playerDAO.checkNearbyPlayersTo(userID, radius)
        aug_list = []
        for player in nearbyPlayersList:
            if player["userID"] != userID:
                player_dict = {'userID':player["userID"],
                               'alignment':player["alignment"],
                               'isDead':player["isDead"],
                               'votedAgainst':player["votedAgainst"],
                               'location':player["location_2d"],
                               'isAdmin':player["isAdmin"],
                               'points':player["points"]
                               }
                aug_list.append(player_dict)
                
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
        PLAYERS_COLLECTION.update({}, {"$set": {"votedAgainst":"None"}}, upsert=False, multi=True)
        PLAYERS_COLLECTION.update({}, {"$set": {"isDead":False}}, upsert=False, multi=True)
        startGame(userID, new_freq)
        return True
    else:
        #means that player that initiated restart was NOT admin
        return False

def concludeGame():
    GAMES_COLLECTION.remove()
    KILLS_COLLECTION.remove()
    PLAYERS_COLLECTION.remove()
    return True

def getAllAlivePlayers():
    alive_players_list = []
    for player in PLAYERS_COLLECTION.find():
        if player["isDead"] == False:
            player_dict = {'userID':player["userID"],
                               'alignment':player["alignment"],
                               'isDead':player["isDead"],
                               'votedAgainst':player["votedAgainst"],
                               'location':player["location_2d"],
                               'isAdmin':player["isAdmin"],
                               'points':player["points"]
                               }
            alive_players_list.append(player_dict)
    return alive_players_list
    
def getVotablePlayers():
    votable_players_list = getAllAlivePlayers()
    return votable_players_list

#places vote if voter is a Townsperson
def placeVote(voter_userID, votee_userID):
    cur_player = playerDAO.getPlayer(voter_userID)
    playerDAO.updatePlayer(voter_userID, "votedAgainst", votee_userID)
    return True

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
    
    player_dict = {'userID':cur_highscore_player["userID"],
                               'alignment':cur_highscore_player["alignment"],
                               'isDead':cur_highscore_player["isDead"],
                               'votedAgainst':cur_highscore_player["votedAgainst"],
                               'location':cur_highscore_player["location_2d"],
                               'isAdmin':cur_highscore_player["isAdmin"],
                               'points':cur_highscore_player["points"]
                               }        
    return player_dict

#sets up the game, once amount of players is known, and gets current coordinates, as well as sets proper TP/WW ratio
def initializeGame():
    all_players = []
    for player in PLAYERS_COLLECTION.find():
        all_players.append(player)
        
    needed_werewolves = len(all_players) / 3
    
    count = 0
    rand_number_list = []
    while count != needed_werewolves:
        rand = randrange(0, len(all_players))
        if rand in rand_number_list:
            continue
        else:
            rand_number_list.append(rand)
            count += 1
            
    for i in rand_number_list:
        cur_player_id = (all_players[i])["userID"]
        playerDAO.updatePlayer(cur_player_id, "alignment", "Werewolf")
    
    if count > 0:
        GAMES_COLLECTION.update({}, {"$set": {"isActive": True}})
        return True
    else:
        return False

def getNumberOfKills():
    total_kills = KILLS_COLLECTION.count()
    return total_kills

def wipeDatabase():
    #FOR TESTING PURPOSES ONLY!!!! Not linked to any URL; must be manually configured
    GAMES_COLLECTION.remove()
    PLAYERS_COLLECTION.remove()
    USERS_COLLECTION.remove()
    KILLS_COLLECTION.remove()

