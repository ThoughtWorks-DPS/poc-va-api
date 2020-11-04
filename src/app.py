from flasgger import Swagger, swag_from
from flask import Flask

app = Flask(__name__)

app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "POC-VA-API",
    "description": "POC api"
}

swagger = Swagger(app)


@app.route('/')
@swag_from('static/hello_world.yml')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
@swag_from('static/hello.yml')
def hello():
    return 'Hello from the API!'

if __name__ == "__main__":
    app.run()
