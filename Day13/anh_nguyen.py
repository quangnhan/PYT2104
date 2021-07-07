import requests
import threading
from datetime import datetime
from database import Database

# #Database
# db = Database()
# humans = db.get("2")
# list_mockapi = db.get_mockapis()
# start = datetime.now()

# def post_data(api, human):
#     # name = api['name']
#     print("Start", human["id"])
#     response = requests.post(api, data=human)
#     print("End", human["id"], response)

# start = datetime.now()
# threads = []

# for api in list_mockapi:
#     t = threading.Thread(target=post_data, args=(api["url"], humans))
#     t.start()
#     threads.append(t)

# print(f"Done : {datetime.now() - start}")


db = Database()
humans = db.get()
list_mockapi = db.get_mockapis()
start = datetime.now()
url = "https://60e1a9545a5596001730f19b.mockapi.io/human"

def post_data(api, human):
    print("Start", human["id"])
    response = requests.post(api, data=human)
    print("End", human["id"], response)

start = datetime.now()
threads = []

for human in humans:
    t = threading.Thread(target=post_data, args=(url, human))
    t.start()
    threads.append(t)

print(f"Done : {datetime.now() - start}")