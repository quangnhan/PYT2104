import requests
from pprint import pprint

url = "https://60e1a9c75a5596001730f1a4.mockapi.io/human"
id = 2
new_data = {
    "name": "Thanh",
    "age": 25,
}
response = requests.put(f"{url}/{id}",data = new_data)
data = response.json()

pprint(data)