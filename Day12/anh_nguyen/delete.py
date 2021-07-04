from pprint import pprint
import requests
import json

url = "https://60e1a9545a5596001730f19b.mockapi.io/human"

id = 2

response = requests.delete(f"{url}/{id}")
data = response.json()

pprint(data)