import requests
import threading
from datetime import datetime
from database import Database
from concurrent.futures import ProcessPoolExecutor

#Database
db = Database()
humans = db.get()

#Post data
url = "https://60e1a9c05a5596001730f19e.mockapi.io/human"
count = 0

def post_data(human):
    global count 
    
    print("Start", human["id"], count)
    response = requests.post(url, data=human)

    if response.status_code == 201:
        count += 1

    print("End", human["id"], response, count)

if __name__ == "__main__":
    start = datetime.now()
    threads = []
    
    executor = ProcessPoolExecutor(max_workers=3)

    for human in humans:
        executor.submit(post_data, (human))
        # t = threading.Thread(target=post_data, args=(human,))
        # t.start() # worker
        # threads.append(t)

    # for t in threads:
    #     t.join()

    executor.shutdown()

    print(f"Count : {count} Done : {datetime.now() - start}")