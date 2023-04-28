import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Hello World"})
# get_response = requests.post(endpoint, json={"title": None, "content": "Hello World"}) => title cant be null
# get_response = requests.post(endpoint, json={"title": "abc", "content": "Hello World", "price":"abc123"}) => must be a valid number
print(get_response.json())