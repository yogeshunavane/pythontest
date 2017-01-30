from flask_pymongo import PyMongo
from flask import Flask, render_template, url_for, request, session, redirect

from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'pymongotest'
app.config['MONGO_URI'] = 'mongodb://mike:l660970@ds137759.mlab.com:37759/pymongotest'

mongo = PyMongo(app)

# @app.route('/add')
# def add():
#     dummy  = mongo.db.dummy
#     dummy.insert({'name':'one','number':'1'})
#     dummy.insert({'name': 'two', 'number': '2'})
#     dummy.insert({'name': 'three', 'number': '3'})
#     dummy.insert({'name': 'four', 'number': '4'})
#     return 'Added user~!'

@app.route('/', methods=['POST'])
def index():

    number = mongo.db.dummy
    result = number.find()

    return dumps(result)

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)