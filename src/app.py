from flask import Flask
from flask import Flask, jsonify
import os
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
@swag_from('static/hello_world.yml')
def hello_world():
    return 'Hello, World!'
