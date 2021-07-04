import json
import requests
from pprint import pprint

url ="https://60e1a9c45a5596001730f1a0.mockapi.io/human"
new_data={
    "name":"Khac Son",
    "age": 21,
},
response = requests.post(url,data=new_data)
data= response.json()

pprint(data)
