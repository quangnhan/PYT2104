import requests

url = "https://60e1a9ca5a5596001730f1a6.mockapi.io/human"
new_data = {
    "name": "vhung",
    "age": 99,
}
response = requests.post(url, data = new_data)
