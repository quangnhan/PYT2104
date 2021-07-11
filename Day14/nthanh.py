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
        

if __name__ == "__main__":
    id = "2"
    server = Server()
    print(server.get_by_id(id))
    

