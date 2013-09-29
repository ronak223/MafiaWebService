from pymongo import MongoClient, GEO2D
import os

CLIENT = MongoClient(os.environ.get('MONGOHQ_URL'))
DB = CLIENT.app18266596
USERS_COLLECTION = DB.users
PLAYERS_COLLECTION = DB.players
GAMES_COLLECTION = DB.games
KILLS_COLLECTION = DB.kills

#setting pymongo geospatial location interpretation
#PLAYERS_COLLECTION.create_index([("location", GEO2D)])
#KILLS_COLLECTION.create_index([("location", GEO2D)])
