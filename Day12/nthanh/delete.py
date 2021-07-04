import requests
from pprint import pprint

url = "https://60e1a9c75a5596001730f1a4.mockapi.io/human"
id = 2

response = requests.delete(f"{url}/{id}")
data = response.json()

pprint(data)