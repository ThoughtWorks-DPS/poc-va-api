from flask import Flask
from flask import Flask, jsonify
import os
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def hello_world():
    """Endpoint returning hello world
        ---
        summary: Returns 'Hello World!'
        responses:
          200:
            description: OK
            schema:
              id: hello_world
              type: string
        """
    return 'Hello, World!'
