import pytest
import requests
from src import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True

    with app.app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get('/')
    assert response.data.decode('utf-8') == 'Hello, World!'
    assert response.status == '200 OK'


@pytest.mark.skip(reason="WIP")
def test_dockerfile():
    response = requests.get("http://127.0.0.1:5000/")

    assert response.status_code == 200
