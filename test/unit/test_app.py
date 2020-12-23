import pytest
import os

from src import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client


def test_hello_from_api(client):
    response = client.get ('/teams/hello')
    assert response.data.decode('utf-8') == 'Hello from the API!'
    assert response.status == '200 OK'


def test_health_endpoint(client):
    response = client.get('/teams/health')
    response_json = response.get_json()
    assert response_json["status"] == 'success'
    assert response.status == '200 OK'


def test_info_endpoint(client):
    os.environ["SEM_VERSION"] = "1.0.0"
    os.environ["GIT_HASH"] = "a1b2c3d45e"
    response = client.get('/teams/info')
    response_json = response.get_json()

    assert response_json["application"]["sem_version"] == "1.0.0"
    assert response_json["application"]["git_hash"] == "a1b2c3d45e"
    assert response.status == '200 OK'

