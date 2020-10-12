# POC-VA-API for delivery infrastructure

## Local Environment Setup
#### Install pre-commit
```sh
brew install pre-commit
pre-commit install
```

#### Python virtual environment setup
##### (1) Install PIP
```sh 
python3 -m pip install --user --upgrade pip
python3 -m pip --version
```
##### (2) Install Virtual Env
```sh
python3 -m pip install --user virtualenv
``` 
##### (3) Create and activate poc-va-api virtual env
```sh
python3 -m venv poc-va-api
source poc-va-api/bin/activate
``` 
##### (4) Install dependencies
```sh
pip3 install -r requirements.txt
``` 

### Run Python application
From root of the project:
```sh
FLASK_APP=src/app.py flask run
```

### Run tests
```sh
pytest
```


