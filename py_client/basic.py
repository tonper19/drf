import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"name": "John", "age": 30})
print(get_response.text)
print(get_response.json())
print(get_response.status_code)
