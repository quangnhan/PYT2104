
#GET
import requests
from pprint import pprint

url = "https://60e1aa205a5596001730f1ac.mockapi.io/human"

response = requests.get(url)
data = response.json()

pprint(data)



