"""Main application package."""
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo

from app.secret import MONGO_URI

# Define the WSGI application object
app = Flask(__name__, static_folder='../build', static_url_path='/')

# Serve static build files
@app.route('/home')
@app.route('/explore')
@app.route('/about')
@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/ripplits/<rid>')
def ripplits(rid):
  return app.send_static_file('index.html')

# enable CORS
cors = CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)
db = mongo.db

# Import a module / component using its blueprint handler variable
from app.link.controllers import blueprint as link_module
from app.ripple.controllers import blueprint as ripple_module
from app.user.controllers import blueprint as user_module
from app.organization.controllers import blueprint as org_module

# Register blueprint(s)
app.register_blueprint(link_module)
app.register_blueprint(ripple_module)
app.register_blueprint(user_module)
app.register_blueprint(org_module)
