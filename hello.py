from flask import Flask
from pymongo import MongoClient
from Models.user import User
import os
from DAOs.playersDAO import PlayerDAO
from DAOs.userDAO import UserDAO
from DAOs.killsDAO import KillDAO
from DAOs.gamesDAO import GameDAO
from Models.players import *
from Models.user import *
from Models.kills import *
from Service.GameService import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    test_user = User()
    test_user.setUsername("Ronak")
    test_user.setPassword("testpass")
    
    client = MongoClient(os.environ.get('MONGOHQ_URL'))
    db = client.app18266596
    users_collection = db.users
    
    cur_user = {"name": test_user.getUsername(),
                "password": test_user.getHashedPassword()
                }
    
    users_collection.insert(cur_user)
    #test_user.sendToDb()
    '''
    test_playerDAO = PlayerDAO()
    test_usersDAO = UserDAO()
    test_killsDAO = KillDAO()
    test_gameDAO = GameDAO()
    
    #startGame("ronak223", 20)
    
    #temp_list = playersNearTo("ronak223", 10)
    #count = len(temp_list)
    
    #test_playerDAO.updatePlayer("brosciusko", "isDead", True)

    restartGame("ronak223", 16)
    '''
    test_kill = Kill()
    test_kill.setLocation(50, -190)
    test_kill.setKillerID("ronak223")
    test_kill.setVictimID("kevinwilliamson")
    test_kill.setTimestamp()
    
    test_killsDAO.registerKill(test_kill)
    '''
    
    '''
    test_player = Player()
    test_player.setUserID("brosciusko")
    test_player.setAlignment("Townsperson")
    test_player.setLocation(10, -59)
    test_player.makeAdmin()
    test_playerDAO.setPlayer(test_player)
    '''
    
    #test_user = User()
    #test_user.setUserID("ronak223")
    #test_user.setPassword("ronakp")
    
    #test_usersDAO.registerUser(test_user)
    #login_message = test_usersDAO.loginUser("ronak223", "ronakp")
    #login_message = test_usersDAO.isLoggedIn("ronak223")
    #isRegged = test_usersDAO.registerUser(test_user)
    #isLoggedIn = test_usersDAO.loginUser(test_user.getUserID(), test_user.getHashedPassword())
    #test_playerDAO.testDatabase()
    #test_usersDAO.testUserConnection()
    
    
    #return temp_list[0]["userID"]
    #test_player = testingGetPlayer("ronak223")
    return "INDEX PAGE"

@app.route('/hello')
def hello():
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)