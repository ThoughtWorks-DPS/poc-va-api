import requests


def test_dockerfile():
    response = requests.get("http://127.0.0.1:5000/teams/hello")

    assert response.status_code == 200
    assert response.content.decode('utf-8') == "Hello from the API!"


def test_healthcheck():
    response = requests.get("http://127.0.0.1:5000/teams/health")
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["status"] == "success"


def test_info():
    response = requests.get("http://127.0.0.1:5000/teams/info")
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["application"]["SemVersion"] == "1.0.0"
    assert response_json["application"]["GitHash"] == "a1b2c3d45e"
