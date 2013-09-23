from flask import Flask
from pymongo import MongoClient
from Models.user import User

app = Flask(__name__)

@app.route('/')
def index():
    test_user = User()
    test_user.setUsername("Ronak")
    test_user.setPassword("testpass")
    test_user.sendToDb()
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
    
@app.route('/testadd/<int:number>')
def add_this(number):
    cur_sum = number + 10
    return "%d" % cur_sum	


if __name__ == "__main__":
    app.run(debug=True)