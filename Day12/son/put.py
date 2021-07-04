import requests
from pprint import pprint

url = "https://60e1a9c45a5596001730f1a0.mockapi.io/human"
id = 2

new_data = {
    "age": 21,
    "name": "Son",
}

response = requests.put(f"{url}/{id}",json = new_data)
data = response.json()

pprint(data)