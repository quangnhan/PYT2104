import requests
from pprint import pprint

url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"

response = requests.get(url)
data = response.json()

pprint(data)