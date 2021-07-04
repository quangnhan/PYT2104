from pprint import pprint
import requests

url = "https://60e1a9ca5a5596001730f1a6.mockapi.io/human"

id = 2

response = requests.delete(f'{url}/{id}')
