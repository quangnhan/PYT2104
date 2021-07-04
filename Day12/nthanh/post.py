import requests
from pprint import pprint

url = "https://60e1a9c75a5596001730f1a4.mockapi.io/human"
new_data = {
    "name": 25,
    "Thanh": 25,
},
response = requests.post(url,data = new_data)
data = response.json()

pprint(data)