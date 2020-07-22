## Configurations
Create a file `secret.py` in the app directory. Create an Atlas cluster in [MongoDB](https://www.mongodb.com/cloud/atlas). In `secret.py`, provide the Connect URL to your Mongo cluster.
```
MONGO_URI = "mongodb+srv://{your url}"
```

## Project Setup
Clone repository:  
```
$ git clone https://github.com/annie-qiu26/ripple-backend.git
```  
Install from Pipfile:  
```
$ pipenv install
```  
If you don't have the right version of python for pipenv, you can also run:
```
pip install -r requirements.txt
```
Set the `FLASK_APP` and `FLASK_DEBUG` environment variables
```
$ export FLASK_APP=run.py
$ export FLASK_DEBUG=1
```
Activate the Pipenv shell (optional):  
```
$ pipenv shell
``` 
Run Flask app:  
```
$ flask run
```  
Deactivate the Pipenv shell:  
```
$ exit
```  

## Developing
Enter [debug mode](https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode) in Flask:  
```
$ export FLASK_ENV=development
$ flask run
```

## Adding packages
```
$ pipenv install <package>
```

## Helpful Links
Flask API: https://flask.palletsprojects.com/en/1.1.x/api/  
Flask-PyMongo: https://flask-pymongo.readthedocs.io/en/latest/  
Pipenv: https://pipenv-fork.readthedocs.io/en/latest/basics.html  
