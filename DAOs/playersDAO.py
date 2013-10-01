'''
Created on Sep 25, 2013

@author: Ronak
'''
from DAOs import *
from Models.players import Player


class PlayerDAO(object):
    '''
    DAO that will get and set player objects in the mongoDB for future use
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def setPlayer(self, userID, latitude, longitude, alignment):
        #used to set a player object in database
        for player in PLAYERS_COLLECTION.find():
            if player["userID"] == userID:
                return "User %s already registered as Player in this game." % userID
            
        playerObj = Player()
        playerObj.setUserID(userID)
        playerObj.setLocation(latitude, longitude)
        playerObj.setAlignment(alignment)
        
        cur_player = {"userID": playerObj.getUserID(),
                      "alignment": playerObj.getAlignment(),
                      "isDead": playerObj.isDead,
                      "votedAgainst": playerObj.getVotedAgainst(),
                      "location_2d": playerObj.getLocation(),
                      "isAdmin": playerObj.isAdmin,
                      "points": playerObj.getPoints()
                      }
        PLAYERS_COLLECTION.insert(cur_player)
        return "Player for user %s registered." % userID
        
    def getPlayer(self, userID):
        #retrieving player object from database, and returning a newly constructed Player object
        cur_player_dict = PLAYERS_COLLECTION.find_one({"userID": userID})
        #cur_player_obj = cur_player_dict["userID"]
        #cur_player_obj.setPlayerID(userID)
        #cur_player_obj.setAlignment(cur_player_dict["alignment"])
        #cur_player_obj.isDead = cur_player_dict["isDead"]
        #cur_player_obj.votedAgainst = cur_player_dict["votedAgainst"]
        #cur_player_obj.setLocation(cur_player_dict["location"][0], cur_player_dict["location"][1])
        
        return cur_player_dict
    
    def checkNearbyPlayersTo(self, userID, radius):
        nearbyPlayerList = []
        cur_player_dict = PLAYERS_COLLECTION.find_one({"userID": userID})
        for nearbyPlayer in PLAYERS_COLLECTION.find({"location_2d": {"$within": {"$center": [cur_player_dict["location_2d"], radius]}}}):
            nearbyPlayerList.append(nearbyPlayer)
        return nearbyPlayerList    
    
    def updatePlayer(self, userID, field, value):
        PLAYERS_COLLECTION.update({"userID": userID}, {"$set": {field:value}})
        return "%s updated field %s with value %s" % (userID, field, value)
    
    def increasePlayerPoints(self, userID, points):
        PLAYERS_COLLECTION.update({"userID": userID}, {"$inc": {"points": points}})
        return "Increased %s points by %d" % (userID, points)
        
        
    
        
        
        