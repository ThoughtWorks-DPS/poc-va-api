import requests


def test_dockerfile():
    response = requests.get("http://127.0.0.1:5000/teams/hello")

    assert response.status_code == 200
    assert response.content.decode('utf-8') == "Hello from the API!"
