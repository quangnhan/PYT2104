from pprint import pprint
import requests

url = "https://60e1a9ca5a5596001730f1a6.mockapi.io/human"

id = 2
new_data = {
    "name": "vhung",
    "age": 99,
}
response = requests.put(f'{url}/{id}', data = new_data)
