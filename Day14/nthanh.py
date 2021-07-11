import requests
import os
from datetime import datetime
from pprint import pprint
from log import Log

class Server:

    __url = "https://60e484a35bcbca001749ea92.mockapi.io/human"

    def __init__(self):
        self.__log = Log("Thanh")

    def get_by_id(self, id):
        response = {}
        try:
            ok = id ==int(id)
            if not ok:
                raise ValueError
            response = requests.get(f"{self.__url}/{int(id)}").json()
            self.__log.log("INFO", "get thanh cong")
        except ValueError:
            self.__log.log("ERROR", f"id {id} khong phai so")
        except:
            self.__log.log("ERROR", "server khong tra ve du lieu")
        return response
    
    def post(self, post_data):
        try:
            name = post_data['name']
            age = post_data['age']
            response = requests.post(self.__url, data = post_data)
            if response.status_code != 201:
                raise ValueError
            self.__log.log('Info','Send thanh cong')
        except ValueError:
            self.__log.log('Error','Loi gui du lieu')
        except:
            self.__log.log('Error','Khong du truong')
        

if __name__ == "__main__":
    server = Server()
    post_data = {
        "name1": "thanh",
        "age": 99,
    }

    # print(server.get_by_id(2))
    server.post(post_data)
