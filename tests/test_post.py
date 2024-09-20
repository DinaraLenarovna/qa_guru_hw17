import json
import requests
from path import path
from jsonschema import validate


def test_create_user(base_url):
    payload = {
        "name": "ryan",
        "job": "driver"
    }
    response = requests.post(base_url + '/api/users', data=payload)
    assert response.status_code == 201
    assert response.json()['name'] == "ryan"
    assert response.json()['job'] == "driver"

    schema = path('post_create_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


def test_login_successful(base_url):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(base_url + '/api/login', data=payload)
    assert 'token' in response.json()

    schema = path('post_login_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


def test_login_unsuccessful(base_url):
    response = requests.post(base_url + '/api/login', data={"email": "peter@klaven"})
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'
