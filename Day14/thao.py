# import requests
# from datetime import datetime
# from pprint import pprint


# class Exception:
#     def __init__(self, url,log):
#         self.__url = url
#         self.__log = Log
    
#     def get_check(self, id):
#         data = {}   

#         try:
#             ok = id ==int (id) #so sánh kiểm tra
#             if not ok:
#                 raise TypeError
#             response = requests.get(f"{self.__url}/{id}").json()
#             data = response.json()
#             if data == {}:
#                 raise Exception
#         except TypeError:
#             self.__log.log ('ERROR','id không phải kiểu int')
#             print ('id không phải kiểu int')
#         except:
#             self.__log.log('ERROR', 'Server khong tra ve du lieu!')
#             print('Server khong tra ve du lieu!')

#     def post_check(self, post_data):
#         try:
#             name = post_data['name']
#             age = post_data['age']
#             response = requests.post(self.__url, data = post_data)
#             if response.status_code != 201:
#                 raise ValueError
#             self.__log.log('Info','Send thanh cong')
#         except ValueError:
#             print('gui du lieu khong thanh cong')
#             self.__log.log('Error','Loi gui du lieu')
#         except:
#             print('Khong du truong name va age')
#             self.__log.log('Error','Khong du truong')
        
# if __name__ == '__main__':

#     url = "https://60e1a9c05a5596001730f19e.mockapi.io/log"
#     Log = "Thao"
#     ex = Exception()
#     ex.get_check(10)
#     post_data = {
#         "name6": "thao",
#         "age": 96,
#     }



import unittest
from log import Log

class SimpleTest(unittest.TestCase):
    def test_send_log(self):
        string = "abc"
        self.assertEquals(string.upper(),"ABC")

    def test_true (self):
        v =  "True"
        msg = " Khong phai true "
        self.assertTrue(v, msg)
    
    def test_false (self):
        v = "False"
        msg = "Khong phai false"
        self.assertFalse(v, msg)
    