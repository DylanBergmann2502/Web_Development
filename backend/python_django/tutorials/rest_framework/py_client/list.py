import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Enter your username: ")
password = getpass("Enter your password: ")

auth_response = requests.post(auth_endpoint, json={'username':username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {"Authorization": f"Bearer {token}"}
    # = "Authoritzation" : "Bearer 4a8ef9dc955ca2d32855819e549187da0a0ee5e3"
    # need this token to log in, deleting it in the admin page will render it invalid
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)

    # print(get_response.json())
    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print("next url: ", next_url)
    print(results)
    # if next_url is not None:
    #     get_response = requests.get(next_url, headers=headers)

