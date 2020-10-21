from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, jsonify
from flask_swagger import swagger
import os

app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "poc-va-api"
    }
)
app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)


@app.route('/')
def hello_world():
    return 'Hello, World!'
