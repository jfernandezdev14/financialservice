from os import environ

from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = environ.get("MONGO_URI") or 'mongodb://api_user:api_pwd@localhost:27020/financialservice'
mongo_client = PyMongo(app)
db = mongo_client.db
CORS(app)
