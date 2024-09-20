import requests


def test_delete(base_url):
    response = requests.delete(base_url + '/api/users/4')
    assert response.status_code == 204
