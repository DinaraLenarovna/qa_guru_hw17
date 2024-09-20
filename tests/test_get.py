import json
import requests
from path import path
from jsonschema import validate


def test_return_list_of_users(base_url):
    response = requests.get(base_url + '/api/users?page=2')

    body = response.json()
    schema = path('get_list_users.json')
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))

    assert response.status_code == 200


def test_return_single_user(base_url):
    response = requests.get(base_url + '/api/users/7')

    email = "michael.lawson@reqres.in"
    body = response.json()
    schema = path('get_single_user.json')

    assert response.json()['data']['email'] == email
    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_user_not_found(base_url):
    response = requests.get(base_url + '/api/users/27')

    assert response.status_code == 404

