import requests
from pprint import pprint

url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"
id = 3

response = requests.get(f"{url}/{id}")
data = response.json()

pprint(data)