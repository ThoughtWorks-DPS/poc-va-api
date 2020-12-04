import pytest

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

def test_code_climate(client):
    response = client.get ('/teams/hello')
    assert response.data.decode('utf-8') == 'Failing Test'
    assert response.status == '404'

def test_health_endpoint(client):
    response = client.get('/teams/health')
    response_json = response.get_json()
    assert response_json["status"] == 'success'
    assert response.status == '200 OK'