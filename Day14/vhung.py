# import requests
# from log import Log

# class ExceptionDemo:
#     __url = 'https://60e1a9ca5a5596001730f1a6.mockapi.io/human'
#     __log_server = Log('vhung')
    
#     def get_by_id(self, id):
#         data = {} 
#         try:
#             check_int = isinstance(id, int)
#             if not check_int:
#                 raise TypeError
#             response = requests.get(f"{self.__url}/{id}")
#             data = response.json()
#             if data == 'Not found':
#                 raise Exception 
#         except TypeError:
#             self.__log_server.log('ERROR', 'id khong phai kieu int!')
#             print('id khong phai kieu int!')         
#         except:
#             self.__log_server.log('ERROR', 'Server khong tra ve du lieu!')
#             print('Server khong tra ve du lieu!')
            
#         return data

#     def post(self, post_data):  
#         try:
#             name = post_data['name']
#             age = post_data['age']
#             response = requests.post(self.__url, data = post_data)
#             if response.status_code != 201:
#                 raise ValueError
#             self.__log_serverlog_server.log('Info','Send thanh cong')
#         except ValueError:
#             print('gui du lieu khong thanh cong')
#             self.__log_serverlog_server.log('Error','Loi gui du lieu')
#         except:
#             print('Khong du truong name va age')
#             self.__log_server.log('Error','Khong du truong')
        
# if __name__ == '__main__':
#     ex = ExceptionDemo()
#     ex.get_by_id(10)
    
#     post_data = {
#         "name1": "vhung",
#         "age": 99,
#     }
#     ex.post(post_data)

###############################################################################################
import unittest

class SimpleTest(unittest.TestCase):
    def test_1(self):
        a = 4
        self.assertEqual(a, 4)
        
    def test_2(self):
        a = '4'
        self.assertEqual(isinstance(a, int), False)
    
    def test_3(self):
        a = '%432'
        with self.assertRaises(TypeError):
            if not isinstance(a, int):
                raise TypeError
            
    def test_4(self):
        self.assertTrue(5 > 3)
    
    def test_5(self):
        self.assertFalse(5 < 3)
        
    def test_6(self):
        self.assertNotEqual(5, 3)
        