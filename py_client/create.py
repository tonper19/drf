import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "1984",
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
