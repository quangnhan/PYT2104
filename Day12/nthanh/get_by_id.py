import requests
from pprint import pprint

url = "https://60e1a9c75a5596001730f1a4.mockapi.io/human/1"

response = requests.get(url)
data = response.json()

pprint(data)