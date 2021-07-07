import requests
import os
from datetime import datetime
from pprint import pprint


class Server:


    def __init__(self, url):
        self.__url = url

    def get(self):
        data = requests.get(self.__url).json()

        self.log("get")
        
        return data

    def get_by_id(self, id):
        data = requests.get(f"{self.__url}/{id}").json()

        self.log("get_by_id")

        return data

    def post(self, data):
        requests.post(self.__url, data=data)
        print("post thanh cong")

        self.log("post")

    def put(self, id, data):
        requests.put(f"{self.__url}/{id}", data=data)
        print("put thanh cong")

        self.log("put")

    def detele(self, id):
        requests.delete(f"{self.__url}/{id}")
        print("delete thanh cong")

        self.log("delete")

    def log(self, method):
        path = f"{os.getcwd()}./Day12/nthanh/log.txt"
        date = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        log_msg = f"{method} - {date}\n"

        with open(path, 'a') as f_log:
            f_log.write(log_msg)


if __name__ == "__main__":
    url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"
    server = Server(url)

    pprint(server.get())
