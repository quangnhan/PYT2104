import requests
import threading
from datetime import datetime
from database import Database


database = Database()
human_1 = database.get(1)

apis = database.get_mockapis()
count = 0

def post_data(url, name, human):
    global count
    print(f"Start post into {name} mockapi", human["id"])
    response = requests.post(url, data=human)

    if response.status_code == 201:
        count += 1
        print(f"End post into {name} mockapi", human["id"], response)
    else:
        print(f"{name} mockapi raise Error: {response.status_code}")

start = datetime.now()
threads = []

for api in apis:
    t = threading.Thread(target=post_data, args=(api["url"], api["name"], human_1))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Count : {count} Done : {datetime.now() - start}")