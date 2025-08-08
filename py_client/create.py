import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Animal Farm",
    "price": 8.99,
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
