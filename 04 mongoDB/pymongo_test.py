from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'pymongotest'
app.config['MONGO_URI'] = 'mongodb://mike:l660970@ds137149.mlab.com:37149/pymongotest'

mongo = PyMongo(app)

#------------------------------INSERTing values
@app.route('/add')
def add():
    user  = mongo.db.users
    user.insert({'name':'Mani','language':'Python'})
    user.insert({'name': 'Raj', 'language': 'C'})
    user.insert({'name': 'Varun', 'language': 'JSON'})
    user.insert({'name': 'Anu', 'language': 'Haselcast'})
    return 'Added user~!'

#------------------------------SELECTing values
@app.route('/find')
def find():
    user = mongo.db.users
    varun = user.find_one({'name':'Raj'})
    return 'You found ' + varun['name'] + 'language fav = ' + varun['language']

#------------------------------UPDATINGing values
@app.route('/update')
def update():
    user = mongo.db.users
    raj = user.find_one({'name': 'Raj'})
    raj['language'] = 'C++'
    user.save(raj)
    return 'Updated Raj!'

#------------------------------DELETINGing values
@app.route('/delete')
def delete():
    user = mongo.db.users
    anu  = user.find_one({'name':'Anu'})
    user.remove(anu)
    return "removed anu!"

if __name__ == '__main__':
    app.run(debug=True)

