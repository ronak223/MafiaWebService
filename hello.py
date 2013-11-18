import os

from flask import Flask, jsonify, Response, json
from flask_basicauth import BasicAuth
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

#app configs for BasicAuth.local accepted user/pass only set at registration, which is NOt protected
app.config['BASIC_AUTH_USERNAME'] = 'specialkeythatnoonewilleverknow'
app.config['BASIC_AUTH_PASSWORD'] = 'specialerpasswordisawesome'
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
        nearby_list = conf
        return Response(json.dumps(nearby_list),  mimetype='application/json')

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
    return Response(json.dumps(alive_player_list),  mimetype='application/json')


@app.route('/getAllVotablePlayers', methods=['GET', 'POST'])
@basic_auth.required
def getAllVotablePlayers():
    votable_player_list = getVotablePlayers()
    return Response(json.dumps(votable_player_list),  mimetype='application/json')

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
        return "Error: %s not a Werewolf" % killer_userID

@app.route('/getCurrentLocation/<userID>', methods=['GET', 'POST'])
@basic_auth.required
def getLocationOf(userID):
    location_tuple = getCurrentLocation(userID)
    location_json = {'latitude': location_tuple[0],
                     'longitude': location_tuple[1]
                     }
    return jsonify(location_json)

@app.route('/getHighscore', methods=['GET', 'POST'])
@basic_auth.required
def getHighScore():
    conf = getHighscorePlayer()
    resp = jsonify(conf)
    return resp

@app.route('/initGame', methods=['GET', 'POST'])
@basic_auth.required
def initGame():
    conf = initializeGame()
    if conf == True:
        return "true"
    else:
        return "false"
#========================================================#    


#==============ROUTING FOR gamesDAO METHODS==============#
@app.route('/dayNightSwitch', methods=['GET', 'POST'])
@basic_auth.required
def switchGameDayNightState():
    return gameDAO.switchDayNight()

@app.route('/getCurrentGame', methods=['GET', 'POST'])
@basic_auth.required
def getCurrentGame():
    conf = gameDAO.getGame()
    if conf == None:
        return "No games"
    else:
        return jsonify(conf)
    
@app.route('/isGameActive', methods=['GET', 'POST'])
@basic_auth.required
def getGameActivity():
    conf = gamesDAO.getGameActivity()
    if conf == True:
        return "true"
    else:
        return "false"
#========================================================# 


#==============ROUTING FOR killDAO METHODS===============#
@app.route('/getAllKills', methods=['GET', 'POST'])
@basic_auth.required
def getTotalKills():
    kill_list = killsDAO.getAllKills()
    return Response(json.dumps(kill_list),  mimetype='application/json')

    
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

@app.route('/getAllPlayers', methods=['GET', 'POST'])
@basic_auth.required
def getAllPlayers():
    player_list = playerDAO.getAllPlayers()
    jsoned_list = {"response": player_list}
    
    return jsonify(jsoned_list)

@app.route('/getSpecificValue/<userID>/<field>', methods=['GET', 'POST'])
@basic_auth.required
def getSpecificValue(userID, field):
    conf = playerDAO.checkValue(userID, field)
    if conf == True:
        return "true"
    else:
        return "false"
    
@app.route('/updateLocation/<userID>/<latitude>/<longitude>', methods=['GET', 'POST'])
@basic_auth.required
def updateLoc(userID, latitude, longitude):
    playerDAO.updateLocation(userID, latitude, longitude);
#==========================================================# 

#==============ROUTING FOR userDAO METHODS===============#
@app.route('/register/<userID>/<password>', methods=['GET', 'POST'])
def regUser(userID, password):
    #app.config['BASIC_AUTH_USERNAME'] = userID
    #app.config['BASIC_AUTH_PASSWORD'] = password
    return usersDAO.registerUser(userID, password)

@app.route('/login/<userID>/<password>', methods=['GET', 'POST'])
def logInUser(userID, password):
    conf = usersDAO.loginUser(userID, password)
    if(conf == True):
        #app.config['BASIC_AUTH_USERNAME'] = userID
        #app.config['BASIC_AUTH_PASSWORD'] = password
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