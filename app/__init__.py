"""Main application package."""
from flask import Flask
from flask_pymongo import PyMongo

from app import link_node

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
mongo = PyMongo(app)
db = mongo.db

# Import a module / component using its blueprint handler variable
from app.link_node.controllers import blueprint as link_node_module

# Register blueprint(s)
app.register_blueprint(link_node_module)
