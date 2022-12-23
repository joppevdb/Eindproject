import json

import requests


# test posts
def test_create_brewery():
    request_data = {"name": "Westmalle",
                    "address": "Antwerpsesteenweg 496, 2390 Westmalle",
                    "owner_id": "1"}

    response = requests.post("http://127.0.0.1:8000/brewery/", json=request_data)
    if response.status_code == 200:
        assert response.status_code == 200
    else:
        response_directory = response.json()
        assert 'error' in response_directory.keys()


def test_create_beer_for_brewery():
    request_data = {
        "name": "Westmalle triple",
        "volume": 33,
        "alcohol_perc": 9,
        "type": "triple"
    }
    response = requests.post("http://127.0.0.1:8000/brewery/1/beers/", json=request_data)
    if response.status_code == 200:
        assert response.status_code == 200
    else:
        response_directory = response.json()
        assert 'error' in response_directory.keys()


def test_create_owner():
    request_data = {
        "name": "Joppe Van den Broeck",
        "password": "test"
    }
    response = requests.post("http://127.0.0.1:8000/owner/", json=request_data)
    if response.status_code == 200:
        assert response.status_code == 200
    else:
        response_directory = response.json()
        assert 'error' in response_directory.keys()


def test_token():
    request_data = {
        "client_id": "",
        "client_secret": "",
        "scope": "",
        "grant_type": "",
        "refresh_token": "",
        "username": "Joppe Van den Broeck",
        "password": "test"
    }
    response = requests.post("http://127.0.0.1:8000/token", data=request_data)
    print(response.text)
    assert response.status_code == 200


# test gets
def test_get_breweries():
    response = requests.get("http://127.0.0.1:8000/brewery/")
    assert response.status_code == 200


def test_get_brewery():
    response = requests.get("http://127.0.0.1:8000/brewery/Westmalle")
    assert response.status_code == 200


def test_get_beers():
    response = requests.get("http://127.0.0.1:8000/beer/")
    assert response.status_code == 200


def test_get_beer():
    response = requests.get("http://127.0.0.1:8000/beer/{name}?name=Westmalle%20triple")
    assert response.status_code == 200


def test_get_type():
    response = requests.get("http://127.0.0.1:8000/beer/type/{type}?beer_type=triple")
    assert response.status_code == 200


def test_get_beer_by_brewery():
    response = requests.get("http://127.0.0.1:8000/beer/brewery/1")
    assert response.status_code == 200


def test_delete_beer():
    request_data = {
        "client_id": "",
        "client_secret": "",
        "scope": "",
        "grant_type": "",
        "refresh_token": "",
        "username": "Joppe Van den Broeck",
        "password": "test"
    }
    tokenrequest = requests.post("http://127.0.0.1:8000/token", data=request_data)

    print(tokenrequest.text)
    token = json.loads(tokenrequest.text)['access_token']
    headerswithtoken = {
        "accept": "application/json",
        "Authorization": f'Bearer {token}'
    }

    response = requests.delete("http://127.0.0.1:8000/beer/{id}?beer_id=1", headers=headerswithtoken)
    print(response.text)
    assert response.status_code == 200
