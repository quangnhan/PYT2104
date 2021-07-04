#POST
import requests
from pprint import pprint

url = "https://60e1aa205a5596001730f1ac.mockapi.io/human"
new_data = {
    "name": "Thao",
    "age": 25,
}

Response = requests.post(url, data =  new_data)
data = Response.json()
pprint (data)