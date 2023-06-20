from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app
app = Flask(__name__)
app.secret_key = '1q2wdkkfglrgj4'

# db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
