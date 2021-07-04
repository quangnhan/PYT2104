import requests
from pprint import pprint

url = "https://60e1aa205a5596001730f1ac.mockapi.io/human"
id = 2

Response = requests.delete(f"{url}/{id}")
data = Response.json()
pprint (data)