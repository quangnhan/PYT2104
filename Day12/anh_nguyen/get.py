from pprint import pprint
import requests
import json

url = "https://60e1a9545a5596001730f19b.mockapi.io/human"

response = requests.get(url)
data = response.json()

pprint(data)