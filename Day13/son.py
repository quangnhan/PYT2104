from database import Database
import threading
import requests

db = Database()
human = db.get()
url = "https://60e1a9c45a5596001730f1a0.mockapi.io/human"

list_mockapi = db.get_mockapis()
count = 0

def post_data(api, human):
    global count
    print("Start send data", human["id"])
    response = requests.post(api, data=human)
    if response.status_code == 201:
        print("Send data successfully")
        count += 1
    print("End", human["id"], response)
threads = []
for i in human:
    t = threading.Thread(target=post_data, args=(url, i))
    t.start()
    threads.append(t)
#for api in list_mockapi:
#    t = threading.Thread(target=post_data, args=(api["url"],human))
#    t.start()
#    threads.append(t)
for t in threads:
    t.join()

print(f"Count: {count}")