import json
import requests
from path import path
from jsonschema import validate


def test_delete(base_url):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(base_url + '/api/users', data=payload)
    id = response.json()['id']
    delete = requests.delete(base_url + '/api/users/' + id)
    assert delete.status_code == 204
    assert delete.text == ''
