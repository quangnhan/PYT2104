import requests
import threading
from datetime import datetime
from database import Database

#Database
db = Database()
humans = db.get()

#Post data
url = "https://60e1a9c05a5596001730f19e.mockapi.io/human"
count = 0

def post_data(human):
    global count 
    
    print("Start", human["id"])
    response = requests.post(url, data=human)

    if response.status_code == 201:
        count += 1

    print("End", human["id"], response)

start = datetime.now()
threads = []

for human in humans:
    t = threading.Thread(target=post_data, args=(human,))
    t.start()
    threads.append(t)
    # post_data(human)

for t in threads:
    t.join()

print(f"Count : {count} Done : {datetime.now() - start}")