import requests
from pprint import pprint

url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"
new_data = {
    "human": "Tam Minh",
    "age": 26
}

response = requests.post(url, data=new_data)
data = response.json()

pprint(data)