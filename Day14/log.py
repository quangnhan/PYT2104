import requests


class Log:
    __url = "https://60e1a9c05a5596001730f19e.mockapi.io/log"

    def __init__(self, username):
        self.username = username

    """
    This function will send log to server
    We have 3 types: INFO, WARNING, ERROR
    """
    def log(self, type, msg):
        data = {
            "username" : self.username,
            "type" : type,
            "message" : msg
        }
        requests.post(self.__url, data=data)

