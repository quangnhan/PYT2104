import requests
from pprint import pprint

url = "https://60e1a9c05a5596001730f19e.mockapi.io/human"

new_data = {
    "name": "Quang Nhan",
    "age": 26,
}

response = requests.post(url,data = new_data)
data = response.json()

pprint(data)