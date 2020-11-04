import pytest

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

def test_hello_from_api(client):
    response = client.get ('/hello')
    assert response.data.decode('utf-8') == 'Hello from the API!'
    assert response.status == '200 OK'
