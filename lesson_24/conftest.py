import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("fixture_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("fixture_setup.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


@pytest.fixture(scope="class")
def session():
    # Fixture for session with authentication

    session = requests.Session()

    # Performing authentication to receive access token
    auth_url = f"{BASE_URL}/auth"
    credentials = {"username": "test_user", "password": "test_pass"}

    # Use HTTPBasicAuth for authentication
    response = session.post(auth_url, json=credentials, auth=HTTPBasicAuth('test_user',
                                                                           'test_pass'))
    logger.info(f"POST request to {auth_url} returned status {response.status_code}")

    assert response.status_code == 200, "Authentication failed"

    # Getting token
    access_token = response.json().get("access_token")
    assert access_token, "Token is not received"

    # Adding token to session headers
    logger.info(f"Access token: {access_token}")
    session.headers.update({'Authorization': 'Bearer ' + access_token})

    return session
