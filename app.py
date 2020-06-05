from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ripple-dev"
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World!</h1>"

if __name__ == '__main__':
    app.run()
