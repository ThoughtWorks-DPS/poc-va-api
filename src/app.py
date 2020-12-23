from flasgger import Swagger, swag_from
from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump
import os

app = Flask(__name__)

app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "POC-VA-API",
    "description": "POC api"
}

swagger = Swagger(app)
health = HealthCheck(app, "/teams/health")
info = EnvironmentDump(app, "/teams/info", include_python=False, include_os=False,
                       include_process=False, include_config=False)


def application_data():
    return {
        "SemVersion": os.environ.get("SEM_VERSION"),
        "GitHash": os.environ.get("GIT_HASH")
    }


info.add_section("application", application_data)


@app.route('/teams/hello')
@swag_from('static/hello.yml')
def hello():
    return 'Hello from the API!'


if __name__ == "__main__":
    app.run()
