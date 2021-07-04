import requests
from pprint import pprint
from requests.models import Response

url = "https://60e1a9c45a5596001730f1a0.mockapi.io/human"
id=3
Response = requests.delete(f"{url}/{id}")
data = Response.json()

pprint(data)