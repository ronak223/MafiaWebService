import requests

print "Testing Ronak Patel's Mafia Web Service"
print "======================================="

main_user = raw_input("Please input your username for registration: ")
main_password = raw_input("Please input your password for registration: ")

#registering with given parameters
print "Registering you"
print "======================================="
r = requests.get('http://mafia-web-service.herokuapp.com/register/' + main_user + '/' + main_password)
r.content
print

#logging user in
print "Logging you in"
print "======================================="
r = requests.get('http://mafia-web-service.herokuapp.com/login/' + main_user + '/' + main_password)
r.content
print

#creating player for the user
print "Creating player for you"
print "======================================="
r = requests.get('http://mafia-web-service.herokuapp.com/createPlayer/' + main_user + '/' + '100/-100/' + 'Werewolf', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print "Player will be created as a Werewolf, at starting coordinated (100, -100)"
r.content
print

#creating two random other users and associated players for testing purposes
print "Creating two other user/player combinations for testing"
print "======================================="
r = requests.get('http://mafia-web-service.herokuapp.com/register/ronak223/ronakp')
r = requests.get('http://mafia-web-service.herokuapp.com/register/testuser/testpass')
r = requests.get('http://mafia-web-service.herokuapp.com/login/' + main_user + '/' + main_password)
r = requests.get('http://mafia-web-service.herokuapp.com/createPlayer/ronak223/' + '98/-99/' + 'Townsperson', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
r = requests.get('http://mafia-web-service.herokuapp.com/createPlayer/testuser/' + '75/-75/' + 'Townsperson', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print "A user ronak223 was created with an associated player that is a Townsperson at coordinates (98, -99)"
print "A user testuser was created with an assocated player that is a Townsperson at coordinates (75, -75)"
print

#testing getting nearby players
print "Testing nearby players"
print "======================================="
print "Finding players that are in a radius of 5 from your location (100, -100)"
r = requests.get('http://mafia-web-service.herokuapp.com/playersNearTo/' + main_user + '/5', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print "The following are the players found:"
print r.content
print
print "Now, finding plauyers that are in a radius of 50 from your location (100, 100)"
r = requests.get('http://mafia-web-service.herokuapp.com/playersNearTo/' + main_user + '/50', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print "The following are the players found:"
print r.content
print

#testing game creation
print "Testing game creation"
print "======================================="
freq = raw_input("Please input a frequency you would like the game to play on: ")
r = requests.get('http://mafia-web-service.herokuapp.com/startGame/' + main_user + '/' + freq, auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print "You have been made game admin for creating the game"
print

print "Now, we'll try to create another game."
freq = raw_input("Please input a frequency you would like the game to play on: ")
r = requests.get('http://mafia-web-service.herokuapp.com/startGame/' + main_user + '/' + freq, auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print

#testing game restart
print "Testing game restart (will only work if you are admin)"
print "======================================="
freq = raw_input("Please input a frequency you would like the game to play on: ")
r = requests.get('http://mafia-web-service.herokuapp.com/restartGame/' + main_user + '/' + freq, auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print

#testing all alive players
print "Testing if all alive players will be returned"
print "======================================="
r = requests.get('http://mafia-web-service.herokuapp.com/getAllAlivePlayers', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print

#testing all votable players
print "Testing if all votable players will be returned"
print "======================================="
r = requests.get('http://mafia-web-service.herokuapp.com/getAllVotablePlayers', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print

#testing kill
print "Testing player kill"
print "======================================="
print "Having your player (Werewolf) kill ronak223's player (Townsperson)" 
r = requests.get('http://mafia-web-service.herokuapp.com/killPlayer/' + main_user + '/' + 'ronak223', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print

print "Now, will re-display all alive players. Should no longer show ronak223"
r = requests.get('http://mafia-web-service.herokuapp.com/getAllAlivePlayers', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print

#testing voting for player
print "Testing voting for player"
print "======================================="
print "Going to have Testuser's player vote for your player"
r = requests.get('http://mafia-web-service.herokuapp.com/placeVote/testuser/' + main_user, auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print

print "Now, going to try to have your player, who is a Werewolf, try to cast vote on testuser, who is Townsperson. This should fail."
r = requests.get('http://mafia-web-service.herokuapp.com/placeVote/' + main_user + '/testuser', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print

#testing getting location of
print "Testing getting location of player"
print "======================================="
print "Going to test your player's location. Should be (100, -100)"
r = requests.get('http://mafia-web-service.herokuapp.com/getCurrentLocation/' + main_user, auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print

#testing current high score
print "Testing current high score"
print "======================================="
print "Each player is awarded 10 points for a kill. You are the only player to score a kill."
r = requests.get('http://mafia-web-service.herokuapp.com/getHighscore', auth=("specialkeythatnoonewilleverknow", "specialerpasswordisawesome"))
print r.content
print


print "This is the end of the web service testing script."
print "=======================END========================"
 






