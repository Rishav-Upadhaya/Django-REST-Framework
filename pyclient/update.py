import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Product1",
    "price": 100.00
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
