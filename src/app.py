from flasgger import Swagger, swag_from
from flask import Flask
from healthcheck import HealthCheck

app = Flask(__name__)

app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "POC-VA-API",
    "description": "POC api"
}

swagger = Swagger(app)
health = HealthCheck(app, "/health")

@app.route('/hello')
@swag_from('static/hello.yml')
def hello():
    return 'Hello from the API!'

if __name__ == "__main__":
    app.run()