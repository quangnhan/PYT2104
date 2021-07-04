from pprint import pprint
import requests
import json

url = "https://60e1a9545a5596001730f19b.mockapi.io/human"

id = 3

new_data = {
    "name": "Anh Nguyen",
    "age": 30,
}

response = requests.put(f"{url}/{id}", json=new_data)
data = response.json()

pprint(data)