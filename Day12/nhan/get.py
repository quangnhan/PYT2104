import requests
from pprint import pprint

url = "https://600e98dd3bb1d100179df9c4.mockapi.io/candidate"

response = requests.get(url)
data = response.json()

pprint(data)