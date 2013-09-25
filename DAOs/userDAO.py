'''
Created on Sep 25, 2013

@author: Ronak
'''
from DAOs import *

class UserDAO(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def testUserConnection(self):
        cur_user = {"name": "testUser",
                "password": "testPASSWORD"
                }
        USERS_COLLECTION.insert(cur_user)
        
        