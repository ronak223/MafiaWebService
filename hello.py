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


#hello.py serves as a config file that routes all HTTP traffic to appropriate functions/methods
app = Flask(__name__)

#DAO initialization for easy access
playerDAO = PlayerDAO()
usersDAO = UserDAO()
killsDAO = KillDAO()
gameDAO = GameDAO()

    
@app.route('/', methods=['GET', 'POST'])
def index():
    return "INDEX PAGE"

#==============ROUTING FOR GameService METHODS===========#
@app.route('/playersNearTo/<userID>/<int:radius>', methods=['GET', 'POST'])
def getNearbyPlayers(userID, radius):
    conf = playersNearTo(userID, radius)
    if conf == False:
        return "%s is not a werewolf, cannot get nearby players" % userID
    else:
        return conf

@app.route('/startGame/<userID>/<int:freq>', methods=['GET', 'POST'])
def newGame(userID, freq):
    conf = startGame(userID, freq)
    if conf == True:
        return "New game started successfully"
    else:
        return "New game not created: a game is already in progress"
    
@app.route('/restartGame/<userID>/<int:new_freq>', methods=['GET', 'POST'])
def restartCurrentGame(userID, new_freq):
    conf = restartGame(userID, new_freq)
    if conf == True:
        return "Current game restarted successfully. Player configuration preserved."
    else:
        return "Could not restart game, $s does not have admin privaledges" % userID
    
@app.route('/getAllAlivePlayers', methods=['GET', 'POST'])
def getAlivePlayers():
    return getAllAlivePlayers()

@app.route('/getAllVotablePlayers', methods=['GET', 'POST'])
def getAllVotablePlayers():
    return getVotablePlayers()

@app.route('/placeVote/<voter_userID>/<votee_userID>', methods=['GET', 'POST'])
def voteForPlayer(voter_userID, votee_userID):
    conf = placeVote(voter_userID, votee_userID)
    if conf == True:
        return "Vote cast successfully"
    else:
        return "Vote not cast. %s not a Townsperson" % voter_userID

@app.route('/killPlayer/<killer_userID>/<victim_userID>', methods=['GET', 'POST'])
def kill(killer_userID, victim_userID):
    conf = killPlayer(killer_userID, victim_userID)
    if conf == True:
        return "%s killed by %s successfully" % (victim_userID, killer_userID)
    else:
        return "Error: %s not a Werewolf or it is not night time" % killer_userID

@app.route('/getCurrentLocation/<userID>', methods=['GET', 'POST'])
def getLocationOf(userID):
    return getCurrentLocation

@app.route('/getHighscore', methods=['GET', 'POST'])
def getHighScore():
    conf = getHighscorePlayer()
    return "%s has highscore of %d" % (conf["userID"], conf["points"])
#========================================================#    


#==============ROUTING FOR gamesDAO METHODS==============#
@app.route('/dayNightSwitch', methods=['GET', 'POST'])
def switchGameDayNightState():
    return gameDAO.switchDayNight()
#========================================================# 


#==============ROUTING FOR killDAO METHODS===============#
@app.route('/getAllKills', methods=['GET', 'POST'])
def getTotalKills(userID):
    return killsDAO.getAllKills()
#========================================================# 

#==============ROUTING FOR playerDAO METHODS===============#
@app.route('/updatePlayer/<userID>/<field>/<value>', methods=['GET', 'POST'])
def updateSpecificPlayerParam(userID, field, value):
    return playerDAO.updatePlayer(userID, field, value)
    
@app.route('/createPlayer/<userID>/<latitude>/<longitude>/<alignment>', methods=['GET', 'POST'])
def createPlayer(userID, latitude, longitude, alignment):
    return playerDAO.setPlayer(userID, float(latitude), float(longitude), alignment)
#==========================================================# 

#==============ROUTING FOR userDAO METHODS===============#
@app.route('/register/<userID>/<password>', methods=['GET', 'POST'])
def regUser(userID, password):
    return usersDAO.registerUser(userID, password)

@app.route('/login/<userID>/<password>', methods=['GET', 'POST'])
def logInUser(userID, password):
    conf = usersDAO.loginUser(userID, password)
    if(conf == True):
        return "Logged in succesfully"
    else:
        return "Login unsuccessful"

@app.route('/logout/<userID>', methods=['GET', 'POST'])
def logOutUser(userID):
    conf = usersDAO.logoutUser(userID)
    if conf == True:
        return "%s logged out successfully" % userID
#========================================================# 

#==============METHODS FOR BASIC AUTHORIZATION===============#

#============================================================# 

if __name__ == "__main__":
    app.run(debug=True)