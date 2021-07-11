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

    def get_by_id(self, id):
        response = {}
        try:
            ok = id ==int(id)
            if not ok:
                raise ValueError
            response = requests.get(f"{self.__url}/{int(id)}").json()
            self.__log.log("INFO", "get successful")
        except ValueError:
            self.__log.log("ERROR", f"id {id} khong phai so")
        except:
            self.__log.log("ERROR", "server fail")
        return response
        

    def post(self, data):
        try:
            if not data["age"] or not data["name"]:
                raise Exception
            requests.post(self.__url, data=data)
            self.__log.log("INFO", "post data successful")
            print(data["age"], data["name"])
        except:
            self.__log.log("ERROR", "data fail")

if __name__ == "__main__":
    data = {
        "age" : "21",
        "name" : "Anh"
    }
    theanh = Server()
    theanh.get_by_id("1a")
    theanh.post(data )