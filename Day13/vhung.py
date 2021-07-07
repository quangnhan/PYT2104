import threading
import requests
from database import Database
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

db = Database()
list_human = db.get()
list_mockapi = db.get_mockapis()


# def post_data(human, api):
#     global count
#     name = api['name']
#     print("Start", name)
#     response = requests.post(api['url'], data=human)
#     print("End", api["name"], response)
#     if response.status_code == 201:
#         print(f'{name} ok!')
#         count += 1

# for api in list_mockapi:
#     t = threading.Thread(target=post_data, args=(human, api,))
#     t.start()
#     threads.append(t)

def post_data(human):
    global count
    name = human['name']
    url = f'https://60e1a9ca5a5596001730f1a6.mockapi.io/human'
    print("Start", name)
    response = requests.post(url, data = human)
    print("End", name, response)
    if response.status_code == 201:
        print(f'{name} ok!')
        count += 1

if __name__ == "__main__":
    threads = []
    count = 0 
    
    # ProcessPoolExecutor runs each of your workers in its own separate child process.
    # ThreadPoolExecutor runs each of your workers in separate threads within the main process.
    
    # executor = ProcessPoolExecutor(max_workers = 3)
    executor = ThreadPoolExecutor(max_workers = 3) 
    for human in list_human:
        executor.submit(post_data, (human))
    executor.shutdown()
    
    # for human in list_human:    
    #     t = threading.Thread(target=post_data, args=(human,))
    #     t.start()
    #     threads.append(t)

    # for t in threads:
    #     t.join()

    print(f'Count: {count}')