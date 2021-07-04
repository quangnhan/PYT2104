# get 
import requests
from pprint import pprint

url = "https://60e1a9d05a5596001730f1aa.mockapi.io/humann"
print('343')
data = requests.get(url).json()
print("duoi data")
print(data)