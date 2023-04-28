import requests

endpoint1 = "http://httpbin.org"
endpoint2 = "http://httpbin.org/anything"

# regular HTTP Request(Non api request) -> HTML
get_response = requests.get(endpoint1)  # HTTP request
print(get_response.text)  # print html

# rest api http request -> JSON(or xml or other formats)
get_response = requests.get(endpoint2, data={"query":"Hello World"})  # rest api HTTP request
print(get_response.json())  # print json -> python dict
print(get_response.status_code)






