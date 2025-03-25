import requests
from getpass import getpass

username = input("What is your username?:")
password = getpass("\nEnter Your Password:")


auth_endpoint = "http://localhost:8000/api/auth/"


auth_response = requests.post(auth_endpoint, json = {'username': username, 'password':password})
print(auth_response.json())


if auth_response.status_code == 200:
    auth_token = auth_response.json()['token']
    headers = {
        "Authorization" : f"Bearer {auth_token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    data = {
        "title": "Product11",
        "price": 439.45
    }
    get_response = requests.get(endpoint, headers=headers)
    # get_response = requests.post(endpoint, json=data)

    print(get_response.json())
