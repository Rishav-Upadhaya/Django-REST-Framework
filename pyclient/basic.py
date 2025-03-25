import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
# endpoint = "http://localhost:8000/api/"

# get_request = requests.get(endpoint, params={"title":"Hello World!"}, json={"query": "Hello World!"})

#Part 1
# print(get_request) #Gives Status Code
# print(get_request.text) # Gives HTML FILE / SOURCE CODE
# print(get_request.json()) # Gives JSON Response
# print(get_request.json()["params"]["abc"])
# print(get_request.json()["query"])
# print(get_request.json())

# # Search by title

# endpoint = "http://localhost:8000/api/"
# find_data = requests.get(endpoint, params={"title":"Product2"})

# print(find_data.json())

# endpoint = "http://localhost:8000/api/"

# get_request = requests.post(endpoint, json={"title" : "ABC123","content":"Hello World!"})

# print(get_request.json())
# print(get_request.status_code)

create = "http://localhost:8000/api/products/"
read = "http://localhost:8000/api/products/17/"
update = "http://localhost:8000/api/products/17/update/"
delete = "http://localhost:8000/api/products/17/delete/"

get_request = requests.post(create, json={"title" : "ABC123","content":"Hello World!"})
print("Create: ", get_request.json())

get_request = requests.get(read)
print("Read: ", get_request.json()) 

get_request = requests.put(update, json={"title" : "ABC123","content":"Hello World!"})
print("Update: ", get_request.json())

get_request = requests.delete(delete)   
print("Delete: ", get_request.status_code, get_request.status_code==204)
