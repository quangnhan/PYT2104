import requests
from pprint import pprint

url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"
id = 5

new_data = {
    "age": 30,
    "human": "Minh",
}

response = requests.put(f"{url}/{id}", json = new_data)
data = response.json()

pprint(data)