from database import Database
import threading
import requests

db = Database()
human = db.get(1)

list_mockapi = db.get_mockapis()

def post_data(api, human):
    response = requests.post(api, data=human)

for api in list_mockapi:
    t = threading.Thread(target=post_data, args=(human,))
    t.start()
