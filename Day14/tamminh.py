import requests
from log import Log


class Server:

    def __init__(self):
        self.__url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"
        self.__log = Log("Minh")

    def get_by_id(self, id):
        response = {}

        try:
            if not isinstance(id, int):
                raise TypeError

            response = requests.get(f"{self.__url}/{id}")

            if response:
                raise Exception
            
            response = response.json()

            self.__log.log("INFO", "get thanh cong")
        except TypeError:
            self.__log.log("ERROR", f"id {id} khong phai so")
        except:
            self.__log.log("ERROR", "server khong tra ve du lieu")

        return response

    def post(self, data):
        try:
            if not data.get("age") or not data.get("name"):
                raise Exception

            response = requests.post(self.__url, data=data)

            if response.status_code != 201:
                raise ValueError

            self.__log.log("INFO", "post data thanh cong")
        except ValueError:
            self.__log.log("ERROR", "loi server")
        except:
            self.__log.log("ERROR", "data khong hop le")

if __name__ == "__main__":
    data = {
        "age" : "25",
        "name" : "Minh"
    }
    sv = Server()
    sv.get_by_id(1)
    # sv.post(data)