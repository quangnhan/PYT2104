import requests
import threading
from datetime import datetime
from database import Database

#Database
db = Database()
human = db.get(1)

list_mockapi = db.get_mockapis()

#Post data
count = 0

def post_data(api, human):
    global count 
    
    print("Start", human["id"])
    response = requests.post(api, data=human)

    if response.status_code == 201:
        count += 1

    print("End", human["id"], response)

start = datetime.now()
threads = []

for api in list_mockapi:
    t = threading.Thread(target=post_data, args=(api["url"], human))
    t.start()
    threads.append(t)
    # post_data(human)

for t in threads:
    t.join()

print(f"Count : {count} Done : {datetime.now() - start}")