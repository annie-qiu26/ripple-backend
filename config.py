# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Database configurations for MongoDB
MONGO_URI = "mongodb://localhost:27017/ripple-dev"
