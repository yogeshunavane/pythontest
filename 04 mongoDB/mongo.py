from flask import Flask
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)


app.config['MONGOALCHEMY_DATABASE'] = 'pymongotest'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://mike:l660970@ds135669.mlab.com:35669/pymongotest'

db = MongoAlchemy(app)

class User(db.Document):
    name = db.StringField()
    password = db.StringField()