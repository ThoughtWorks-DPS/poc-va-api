import pytest
import yaml

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

# def test_hello_world_documentation(client):
#     response = client.get('/')
#
#     with open(r'/Users/punitlad/projects/va/dps/di/poc/poc-va-api/src/static/hello_world.yml') as file:
#         documentation = yaml.load(file)
#         assert documentation['responses'][200] == # get the key for 200 check status
#         print(documentation)
# #         doc_response = documentation['responses']['200']
# #         println(doc_response)
#
# #     assert response.status == doc_response

