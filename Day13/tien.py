import requests
import threading
from datetime import datetime
from database import Database

db = Database()
humans = db.get()
my_url = "https://60e1a9d05a5596001730f1aa.mockapi.io/humann"

threads = []

count = 0

def post_data(api,human):
    global count
    print("Start send data", human["id"])
    response = requests.post(api,human)
    if response.status_code == 201:
        print("successfully")
        count += 1
    print("end", human["id"],response)

for person in humans:
    t = threading.Thread(target=post_data, args=(my_url,person))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"count : {count}")

# Day 13 
# import requests
# import threading
# from datetime import datetime
# from database import Database

# db = Database()
# humans = db.get(1)



# list_mockapi = db.get_mockapis()
# count = 0


# def post_data(api,human):
#     global count
#     print("Start send data", human["id"])
#     response = requests.post(api,human)
#     if response.status_code == 201:
#         print("send data successfully")
#         count += 1 
#     print("End",human["id"],response)

# threads = []

# for api in list_mockapi:
#     t = threading.Thread(target=post_data,args=(api["url"],humans))
#     t.start()
#     threads.append(t)

# for  t in threads:
#     t.join()

# print(f'count: {count}')
