from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost/financialservice"
mongo = PyMongo(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
