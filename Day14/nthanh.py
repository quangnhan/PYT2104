import requests
from log import Log
import unittest

# class Server:

#     __url = "https://60e484a35bcbca001749ea92.mockapi.io/human"

#     def __init__(self):
#         self.__log = Log("Thanh")

#     def get_by_id(self, id):
#         response = {}
#         try:
#             ok = id ==int(id)
#             if not ok:
#                 raise ValueError
#             response = requests.get(f"{self.__url}/{int(id)}").json()
#             self.__log.log("INFO", "get thanh cong")
#         except ValueError:
#             self.__log.log("ERROR", f"id {id} khong phai so")
#         except:
#             self.__log.log("ERROR", "server khong tra ve du lieu")
#         return response
    
#     def post(self, post_data):
#         try:
#             name = post_data['name']
#             age = post_data['age']
#             response = requests.post(self.__url, data = post_data)
#             if response.status_code != 201:
#                 raise ValueError
#             self.__log.log('Info','Post thanh cong')
#             return response
#         except ValueError:
#             self.__log.log('Error','Loi gui du lieu')
#         except:
#             self.__log.log('Error','Khong du truong')
        
class SimpleTest(unittest.TestCase):
    def test_id(self):
        id = 1
        self.assertEqual(id,2)

    def test_boolean(self):
        ok = True
        self.assertTrue(ok)

# if __name__ == "__main__":
    # server = Server()
    # post_data = {
    #     "name": "thanh",
    #     "age": 99,
    # }

    # # print(server.get_by_id(2))
    # print(server.post(post_data))
