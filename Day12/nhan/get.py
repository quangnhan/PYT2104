import requests
from pprint import pprint

url = "https://60e1a9c05a5596001730f19e.mockapi.io/human"

response = requests.get(url)
data = response.json()

pprint(data)