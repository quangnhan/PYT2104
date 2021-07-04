import requests
from pprint import pprint

url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"
id = 2

response = requests.delete(f"{url}/{id}")
data = response.json()

pprint(data)