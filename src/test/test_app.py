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
