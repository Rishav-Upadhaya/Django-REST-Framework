import requests
from getpass import getpass

username = input("What is your username?:")
password = getpass("\nEnter Your Password:")


auth_endpoint = "http://localhost:8000/api/token/"


auth_response = requests.post(auth_endpoint, json = {'username': username, 'password':password})
print(auth_response.json())


if auth_response.status_code == 200:
    auth_token = auth_response.json()['access']
    actions = {
        "label" : f"Token {auth_token}"
    }
    endpoint = "http://localhost:8000/api/token/verify/"

    token_data = {
        "token": auth_token
    }
    get_response = requests.post(endpoint, json=token_data)
    # get_response = requests.post(endpoint, json=data)

    print(get_response.status_code)
