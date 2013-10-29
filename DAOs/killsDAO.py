'''
Created on Sep 25, 2013

@author: Ronak
'''
from DAOs import *
from Models.kills import Kill

class KillDAO(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def registerKill(self, killObj):
        #registers a single kill in DB
        #TODO: Figure out why location won't work here!
        cur_kill = {"killerID": killObj.getKillerID(),
                      "victimID": killObj.getVictimID(),
                      "timestamp": killObj.getTimestamp(),
                      "location_2d": killObj.getLocation()
                      }
        
        KILLS_COLLECTION.insert(cur_kill)
        
    def getAllKills(self):
        kills_list = []
        for kill in KILLS_COLLECTION.find():
            kill_dict = {'killerID': kill["killerID"],
                         'victimID': kill["victimID"],
                         'location': kill["location_2d"],
                         'timestamp': kill["timestamp"]
                         }
            kills_list.append(kill_dict)
        return kills_list
            
        