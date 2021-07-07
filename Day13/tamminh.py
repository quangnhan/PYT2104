import requests
import threading
from datetime import datetime
from database import Database


database = Database()
human_1 = database.get(1)

apis = database.get_mockapis()
count = 0

def post_data(url, human):
    global count
    print("Start", human["id"])
    response = requests.post(url, data=human)

    if response.status_code == 201:
        count += 1

    print("End", human["id"], response)

start = datetime.now()
threads = []

for api in apis:
    t = threading.Thread(target=post_data, args=(api["url"], human_1))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Count : {count} Done : {datetime.now() - start}")