import json
import requests
from path import path
from jsonschema import validate


def test_update_user(base_url):
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(base_url + '/api/users/2', data=payload)

    with open(path('put_update_user.json')) as file:
        validate(response.json(), schema=json.loads(file.read()))
    assert response.status_code == 200
    assert response.json()['name'] == 'morpheus'
    assert response.json()['job'] == 'zion resident'
