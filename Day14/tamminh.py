import requests
from log import Log


class Server:

    def __init__(self):
        self.__url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"
        self.__log = Log("Minh")

    def get_by_id(self, id):
        response = {}

        try:

            response = requests.get(f"{self.__url}/{int(id)}").json()
            self.__log.log("INFO", "get thanh cong")
        except:
            self.__log.log("ERROR", f"id {id} khong phai so")

        return response

    def post(self, data):
        try:
            requests.post(self.__url, data=data)
            self.__log.log("INFO", "post data thanh cong")
        except:
            self.__log.log("ERROR", "data khong hop le")

if __name__ == "__main__":
    sv = Server()
    sv.get_by_id("1a")