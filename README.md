## Project Setup
Clone repository:  
```
$ git clone https://github.com/annie-qiu26/ripple-backend.git
```  
Install from Pipfile:  
```
$ pipenv install
```  
Set the `FLASK_APP` and `FLASK_DEBUG` environment variables
```
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
```
Activate the Pipenv shell:  
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