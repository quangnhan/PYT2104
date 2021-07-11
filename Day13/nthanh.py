import requests
import threading
from datetime import datetime
from database import Database
from concurrent.futures import ProcessPoolExecutor

#Database
# db = Database()
# human = db.get(1)
# list_mockapi = db.get_mockapis()
# start = datetime.now()
# threads = []
# count = 0

# def post_data(url, name, human):
#     global count 
#     name = api["name"]
#     print("Start", name)
#     response = requests.post(url, data=human)
#     print("End", name, response)
#     if response.status_code == 201:
#         count += 1
#         print(name, "ok!")
    
# for api in list_mockapi:
#     t = threading.Thread(target=post_data, args=(api["url"],api["name"], human))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()
    
# print(f"Count : {count} Done : {datetime.now() - start}")

db = Database()
humans = db.get()
list_mockapi = db.get_mockapis()
url = "https://60e1a9c05a5596001730f19e.mockapi.io/human"
count = 0

def post_data(human):
    global count 
    print("Start", human["id"])
    response = requests.post(url, data=human)
    print(count)
    print("End", human["id"], response)

    if response.status_code == 201:
        count += 1
    
if __name__=="__main__":    
    start = datetime.now()
    threads = []
    
    executor = ProcessPoolExecutor(max_workers=3)

    for human in humans:
        executor.submit(post_data, (human))
        
    #     t = threading.Thread(target=post_data, args=(url, human))
    #     t.start()
    #     threads.append(t)

    # for t in threads:
    #     t.join()
    executor.shutdown()
    print(f"Count : {count} Done : {datetime.now() - start}")