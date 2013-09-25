from pymongo import MongoClient
import os

CLIENT = MongoClient(os.environ.get('MONGOHQ_URL'))
DB = CLIENT.app18266596
USERS_COLLECTION = DB.users
PLAYERS_COLLECTION = DB.players
GAMES_COLLECTION = DB.games
KILLS_COLLECTION = DB.kills