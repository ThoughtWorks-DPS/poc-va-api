## Local Environment Setup
### Install pre-commit
>  brew install pre-commit
>  pre-commit install

### Virtual environment setup
 Install Pip
 > python3 -m pip install --user --upgrade pip
 Verify pip install
 > python3 -m pip --version
Install Virtual Env
> python3 -m pip install --user virtualenv

### Create poc-va-api virtual env
> python3 -m venv poc-va-api
> source poc-va-api/bin/activate

### Install dependencies
> pip3 install -r requirements.txt

### Run Python application
 From root of the project:
 > FLASK_APP=src/app.py flask run

 ### Run Python tests
 > pytest