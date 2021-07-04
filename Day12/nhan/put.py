import requests
from pprint import pprint

url = "https://60e1a9c05a5596001730f19e.mockapi.io/human"
id = 2

new_data = {
    "age": 30,
    "name": "Quang Nhan 12",
}

response = requests.put(f"{url}/{id}",json = new_data)
data = response.json()

pprint(data)