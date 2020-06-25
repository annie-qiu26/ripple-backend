"""Main application package."""
from flask import Flask
from flask_pymongo import PyMongo

from app.secret import MONGO_URI

# Define the WSGI application object
app = Flask(__name__)

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
