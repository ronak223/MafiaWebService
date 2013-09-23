from flask import Flask
from pymongo import MongoClient, Connection
from Models.user import User
import os


app = Flask(__name__)

def mongo_conn():
    # Format: MONGOHQ_URL: mongodb://<user>:<pass>@<base_url>:<port>/<url_path>
    if os.environ.get('MONGOHQ_URL'):
        return Connection(os.environ['MONGOHQ_URL'])
    else:
        return Connection()

@app.route('/', methods=['GET', 'POST'])
def index():
    test_user = User()
    test_user.setUsername("Ronak")
    test_user.setPassword("testpass")
    connection = mongo_conn()
    db = connection.app18266596
    
    users_collection = db.users
    
    cur_user = {"name": test_user.getUsername(),
                "password": test_user.getHashedPassword()
                }
    
    cur_user_id = users_collection.insert(cur_user)
    #test_user.sendToDb()
    return "" + cur_user_id

@app.route('/hello')
def hello():
    return 'Hello World'
    
@app.route('/testadd/<int:number>')
def add_this(number):
    cur_sum = number + 10
    return "%d" % cur_sum	


if __name__ == "__main__":
    app.run(debug=True)