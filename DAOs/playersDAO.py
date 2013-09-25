'''
Created on Sep 25, 2013

@author: Ronak
'''
from DAOs import *

class PlayerDAO(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def testDatabase(self):
        cur_player = {"name": "testPLAYER",
                "password": "testPASSWORD"
                }
        
        PLAYERS_COLLECTION.insert(cur_player)
        
        
        