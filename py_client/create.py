import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Geografía de Cuba",
    "price": 5.57,
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
