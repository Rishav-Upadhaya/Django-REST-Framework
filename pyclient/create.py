import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Product10",
    "price": 398.76
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
