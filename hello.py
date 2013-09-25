from flask import Flask
from pymongo import MongoClient
from Models.user import User
import os
from DAOs.playersDAO import PlayerDAO
from DAOs.userDAO import UserDAO


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
    
    test_playerDAO.testDatabase()
    test_usersDAO.testUserConnection()
    
    
    return "Index Page"

@app.route('/hello')
def hello():
    return 'Hello World'
    
@app.route('/testadd/<int:number>')
def add_this(number):
    cur_sum = number + 3
    return "%d" % cur_sum	


if __name__ == "__main__":
    app.run(debug=True)