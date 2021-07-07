import threading
import requests
from database import Database

db=Database()
humans = db.get(1)

list_mockapi = db.get_mockapis()

def post_data(api, human):
    print("Start send data", human["id"])
    response = requests.post(api, human)
    if response.status_code == 201:
        print("Send data successfully")
    print("End", human["id"], response)

threads = []
for api in list_mockapi:
    t = threading.Thread(target=post_data, args=(api["url"], humans))
    t.start()
    threads.append(t)