# #!/usr/bin/python
#
# import psycopg2
#
# conn = psycopg2.connect(database="crawldashboard", user="postgres", password="postgres@123", host="127.0.0.1", port="5432")
#
# print "Opened database successfully"


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@123@localhost/flask_movie3'
# db = SQLAlchemy(app)
#
#
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username
# from sqlalchemy import *
# engine = create_engine('postgresql://postgres:postgres@123@localhost/flask_movie3')
#
# metadata = MetaData()
#
# user = Table('users', metadata,
#     Column('user_id', Integer, primary_key=True),
#     Column('user_name', String(16), nullable=False),
#     Column('email_address', String(60), key='email'),
#     Column('password', String(20), nullable=False)
# )
#
# user_prefs = Table('user_prefs', metadata,
#     Column('pref_id', Integer, primary_key=True),
#     Column('user_id', Integer, ForeignKey("users.user_id"), nullable=False),
#     Column('pref_name', String(40), nullable=False),
#     Column('pref_value', String(100))
# )
#
# manager_kunal = Table('manager_kunal', metadata,
#     Column('pref_id', Integer, primary_key=True),
#     Column('user_id', Integer, ForeignKey("users.user_id"), nullable=False),
#     Column('pref_name', String(40), nullable=False),
#     Column('pref_value', String(100))
# )
#
# metadata.create_all(engine)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request,url_for,redirect
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@123@localhost/flask_movie3'
app.debug=True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
db=SQLAlchemy(app)

class sser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


me = sser('admin', 'admin@example.com')
db.session.add(me)
db.session.commit()


if __name__ == '__main__':
    app.run(host= '10.10.5.101', port=9000,debug=True)