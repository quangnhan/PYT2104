import threading
import requests
from database import Database

db = Database()
human = db.get(1)
list_mockapi = db.get_mockapis()
count = 0
threads = []

def post_data(human, api):
    global count
    name = api['name']
    print("Start", name)
    response = requests.post(api['url'], data=human)
    print("End", api["name"], response)
    if response.status_code == 201:
        print(f'{name} ok!')
        count += 1

for api in list_mockapi:
    t = threading.Thread(target=post_data, args=(human, api,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f'Count: {count}')