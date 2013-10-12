import os

from flask import Flask
from pymongo import MongoClient

from DAOs.gamesDAO import GameDAO
from DAOs.killsDAO import KillDAO
from DAOs.playersDAO import PlayerDAO
from DAOs.userDAO import UserDAO
from Models.kills import *
from Models.players import *
from Models.user import *
from Service.GameService import *

from flask_basicauth import BasicAuth

#hello.py serves as a config file that routes all HTTP traffic to appropriate functions/methods
app = Flask(__name__)

#app configs for BasicAuth.local accepted user/pass only set at registration, which is NOt protected
app.config['BASIC_AUTH_USERNAME'] = 'u9123-u9uadaslkjd'
app.config['BASIC_AUTH_PASSWORD'] = '0-9123jkaljddlasd'
basic_auth = BasicAuth(app)

#DAO initialization for easy access
playerDAO = PlayerDAO()
usersDAO = UserDAO()
killsDAO = KillDAO()
gameDAO = GameDAO()

    
@app.route('/')
def index():
    return "Welcome to Ronak's Mafia Game Web Service. Please register/login."

#==============ROUTING FOR GameService METHODS===========#
@app.route('/playersNearTo/<userID>/<int:radius>', methods=['GET', 'POST'])
@basic_auth.required
def getNearbyPlayers(userID, radius):
    conf = playersNearTo(userID, radius)
    if conf == False:
        return "%s is not a werewolf, cannot get nearby players" % userID
    else:
        return conf

@app.route('/startGame/<userID>/<int:freq>', methods=['GET', 'POST'])
@basic_auth.required
def newGame(userID, freq):
    conf = startGame(userID, freq)
    if conf == True:
        return "New game started successfully"
    else:
        return "New game not created: a game is already in progress"
    
@app.route('/restartGame/<userID>/<int:new_freq>', methods=['GET', 'POST'])
@basic_auth.required
def restartCurrentGame(userID, new_freq):
    conf = restartGame(userID, new_freq)
    if conf == True:
        return "Current game restarted successfully. Player configuration preserved."
    else:
        return "Could not restart game, $s does not have admin privaledges" % userID
    
@app.route('/getAllAlivePlayers', methods=['GET', 'POST'])
@basic_auth.required
def getAlivePlayers():
    alive_player_list = getAllAlivePlayers()
    alive_string = ""
    for player in alive_player_list:
        alive_string = alive_string + player['userID'] + ", "

@app.route('/getAllVotablePlayers', methods=['GET', 'POST'])
@basic_auth.required
def getAllVotablePlayers():
    return getVotablePlayers()

@app.route('/placeVote/<voter_userID>/<votee_userID>', methods=['GET', 'POST'])
@basic_auth.required
def voteForPlayer(voter_userID, votee_userID):
    conf = placeVote(voter_userID, votee_userID)
    if conf == True:
        return "Vote cast successfully"
    else:
        return "Vote not cast. %s not a Townsperson" % voter_userID

@app.route('/killPlayer/<killer_userID>/<victim_userID>', methods=['GET', 'POST'])
@basic_auth.required
def kill(killer_userID, victim_userID):
    conf = killPlayer(killer_userID, victim_userID)
    if conf == True:
        return "%s killed by %s successfully" % (victim_userID, killer_userID)
    else:
        return "Error: %s not a Werewolf or it is not night time" % killer_userID

@app.route('/getCurrentLocation/<userID>', methods=['GET', 'POST'])
@basic_auth.required
def getLocationOf(userID):
    return getCurrentLocation

@app.route('/getHighscore', methods=['GET', 'POST'])
@basic_auth.required
def getHighScore():
    conf = getHighscorePlayer()
    return "%s has highscore of %d" % (conf["userID"], conf["points"])
#========================================================#    


#==============ROUTING FOR gamesDAO METHODS==============#
@app.route('/dayNightSwitch', methods=['GET', 'POST'])
@basic_auth.required
def switchGameDayNightState():
    return gameDAO.switchDayNight()
#========================================================# 


#==============ROUTING FOR killDAO METHODS===============#
@app.route('/getAllKills', methods=['GET', 'POST'])
@basic_auth.required
def getTotalKills(userID):
    return killsDAO.getAllKills()
#========================================================# 

#==============ROUTING FOR playerDAO METHODS===============#
@app.route('/updatePlayer/<userID>/<field>/<value>', methods=['GET', 'POST'])
@basic_auth.required
def updateSpecificPlayerParam(userID, field, value):
    return playerDAO.updatePlayer(userID, field, value)
    
@app.route('/createPlayer/<userID>/<latitude>/<longitude>/<alignment>', methods=['GET', 'POST'])
@basic_auth.required
def createPlayer(userID, latitude, longitude, alignment):
    return playerDAO.setPlayer(userID, float(latitude), float(longitude), alignment)
#==========================================================# 

#==============ROUTING FOR userDAO METHODS===============#
@app.route('/register/<userID>/<password>', methods=['GET', 'POST'])
def regUser(userID, password):
    app.config['BASIC_AUTH_USERNAME'] = userID
    app.config['BASIC_AUTH_PASSWORD'] = password
    return usersDAO.registerUser(userID, password)

@app.route('/login/<userID>/<password>', methods=['GET', 'POST'])
def logInUser(userID, password):
    conf = usersDAO.loginUser(userID, password)
    if(conf == True):
        app.config['BASIC_AUTH_USERNAME'] = userID
        app.config['BASIC_AUTH_PASSWORD'] = password
        return "Logged in succesfully"
    else:
        return "Login unsuccessful"

@app.route('/logout/<userID>', methods=['GET', 'POST'])
@basic_auth.required
def logOutUser(userID):
    conf = usersDAO.logoutUser(userID)
    if conf == True:
        return "%s logged out successfully" % userID
#========================================================# 

if __name__ == "__main__":
    app.run(debug=True)