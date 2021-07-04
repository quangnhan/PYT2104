import requests
from pprint import pprint

url = "https://600e98dd3bb1d100179df9c4.mockapi.io/candidate"
new_data = {
    "name": "Quang Nhan",
    "age": 26,
},
response = requests.post(url,data = new_data)
data = response.json()

pprint(data)