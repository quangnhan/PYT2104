# import requests


# class Log:
#     __url = "https://60e1a9cc5a5596001730f1a8.mockapi.io/human"

#     def __init__(self, username):
#         self.username = username

#     """
#     This function will send log to server
#     We have 3 types: INFO, WARNING, ERROR
#     """
#     def log(self, type, msg):
#         data = {
#             "username" : self.username,
#             "type" : type,
#             "message" : msg
#         }
#         requests.post(self.__url, data=data)
 
# 
import requests
from log import Log


class Server:

    def __init__(self):
        self.__url = "https://60e1a9cc5a5596001730f1a8.mockapi.io/human"
        self.__log = Log("theanh")

    def get_id(self, id):
        response = {}

        try:
            check_int = isinstance(id, int)
            print(check_int)
            if not check_int:
             response = requests.get(f"{self.__url}/{id}")
            self.__log.log("INFO", "successful")
        except:
            self.__log.log("ERROR", f"id {id} fail")

        return response

    def post(self, data):
        try:
            requests.post(self.__url, data=data)
            self.__log.log("INFO", "successful")
        except:
            self.__log.log("ERROR", "fail")

if __name__ == "__main__":
    post_data = {
        "name": "theanh",
        "age": 21,
    }
    theanh = Server()
    theanh.get_id("1")