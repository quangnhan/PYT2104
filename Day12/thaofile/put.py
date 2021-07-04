
import requests
from pprint import pprint

url = "https://60e1aa205a5596001730f1ac.mockapi.io/human"
id = 2
new_data = {
    "name": "Thao6",
    "age": 25,
}

Response = requests.put(f"{url}/{id}", json = new_data)
data = Response.json()
pprint (data)