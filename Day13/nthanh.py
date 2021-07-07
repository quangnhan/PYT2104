import requests
import threading
from datetime import datetime
from database import Database

#Database
db = Database()
human = db.get(1)
list_mockapi = db.get_mockapis()
start = datetime.now()
threads = []
count = 0

def post_data(url, name, human):
    global count 
    name = api["name"]
    print("Start", name)
    response = requests.post(url, data=human)
    print("End", name, response)
    if response.status_code == 201:
        count += 1
        print(name, "ok!")
    
for api in list_mockapi:
    t = threading.Thread(target=post_data, args=(api["url"],api["name"], human))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    
print(f"Count : {count} Done : {datetime.now() - start}")