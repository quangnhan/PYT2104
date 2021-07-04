from pprint import pprint
import requests
import json

url = "https://60e1a9545a5596001730f19b.mockapi.io/human"
new_data = {
    "name": "Anh Nguyen",
    "age": 25,
}

response = requests.post(url,data = new_data)
data = response.json()

pprint(data)