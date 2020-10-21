from pathlib import Path
import os
from swagger_tester import swagger_test


def project_root() -> Path:
    return Path(__file__).parent.parent


ROOT_DIR = os.path.dirname(os.path.abspath("swagger.json"))
print('root:: ', ROOT_DIR)

authorize_error = {
    'get': {
        '/': [200]
    }
}

# Run the test with connexion
# An AssertionError will be raise in case of error.
# swagger_test(f'{ROOT_DIR}/test.json', authorize_error=authorize_error)
# swagger_test('/Users/seunoluwaloju/thoughtworks/di/poc-va-api/test.json', authorize_error=authorize_error)


# Or if you have a running API
# swagger_test(app_url='http://localhost:5000/', authorize_error=authorize_error)
