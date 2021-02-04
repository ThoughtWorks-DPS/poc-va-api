# POC-VA-API for delivery infrastructure
[![Maintainability](https://api.codeclimate.com/v1/badges/cdd8fff724faa3eef566/maintainability)](https://codeclimate.com/github/ThoughtWorks-DPS/poc-va-api/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/cdd8fff724faa3eef566/test_coverage)](https://codeclimate.com/github/ThoughtWorks-DPS/poc-va-api/test_coverage)
## Local Environment Setup
#### Install pre-commit
```sh
brew install pre-commit
brew install git-secrets
git-secrets --add-provider -- curl -H 'Cache-Control: no-cache' https://raw.githubusercontent.com/ThoughtWorks-DPS/poc-resources/main/git-secrets-pattern.txt
pre-commit install -f 
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

### Build and run docker image
From root of the project:
```sh
make GIT_HASH="$(git rev-parse --short HEAD)" app
```

### Running tests
Run unit test
```sh
make unit-test
```
Run integration tests
```sh
make GIT_HASH="$(git rev-parse --short HEAD)" integration-test
```
Run swagger tests
```sh
make GIT_HASH="$(git rev-parse --short HEAD)" swagger-test
```

### Deploy to local kubernetes cluster
#### (1) Install Helm
```sh
brew install helm
```
#### (2) Install minikube
```sh
brew install minikube
```
```sh
minikube start
```
#### (3) Run cluster setup (first time)
##### Create namespace
```sh
chmod +x create_namespaces.sh
./create_namespaces.sh
```
##### Create secrets
```sh
chmod +x ../poc-platform-eks/tpl/create_cluster_secrets.sh
../poc-platform-eks/tpl/create_cluster_secrets.sh
```
##### Helm deploy
```sh
helm upgrade --install poc-va-api helm --set image.tag=${CIRCLE_SHA1:0:7} -n di-dev
```
#### Port Forward (withour ISTIO)
```sh
kubectl port-forward ${POD_NAME} 5000:5000 -n di-dev
```
##### Helm uninstall
```sh
helm delete poc-va-api -n di-dev
```
