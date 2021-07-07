# from database import Database
# import threading
# import requests

# db=Database()
# humans = db.get(1)

# list_mockapi = db.get_mockapis()

# def post_data(api, human):
#     print("Start", human["id"])
#     response = requests.post(api, human)
#     if response.status_code == 201:
#      print("successfully")
#     print("End", human["id"], response)

# threads = []
# for api in list_mockapi:
#     t = threading.Thread(target=post_data, args=(api["url"], humans))
#     t.start()
#     threads.append(t)

import requests
import threading
from datetime import datetime
from database import Database

#Database
db = Database()
humans = db.get()

#Post data
url = "https://60e1a9cc5a5596001730f1a8.mockapi.io/human"
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