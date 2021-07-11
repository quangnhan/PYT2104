import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('me'.upper(), 'ME')

    def test_isupper(self):
        self.assertTrue('ME'.isupper())
        self.assertFalse('Me'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        
        
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()




# import requests
# from pprint import pprint, pp
# from typing import Type
# from log import Log

# class Server():

#     url = 'https://60e1a9d05a5596001730f1aa.mockapi.io/humann'
#     id = ''
#     data = ''   
    
#     def __init__(self,url,id,data):
#         self.__url = url
    
#     def get(self,id):
#         data = requests.get(self.__url).json()
#         dataid = requests.get(f'{url}/{id}').json()

#         try :
#             ok = id ==int(id)

#             if not ok:
#                 raise Exception
#         except:
#             print("[]")


#         self.log("get")
#         return data,dataid

#     def post(self,data):
#         requests.post(self.__url,data = data).json()
#         print('post successfully')
#         self.log("post")

#     def put(self,data,id):
#         requests.put(f'{self.__url}/{id}',data = data).json()
#         print('put successfully')

#         self.log("put")

#     def delete(self,id):
#         requests.delete(f'{self.__url}/{id}').json()
#         print('delete successfully')

#         self.log("delete")

#     def log(self, method):
#         path = f"{os.getcwd()}/Day12/tien/log.txt"
        
#         date = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        
#         log_msg = f"{method} - {date}\n"

#         with open(path, 'a') as f_log:
#             f_log.write(log_msg)


    
