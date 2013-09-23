from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
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