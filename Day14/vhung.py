from typing import Type
import requests
from pprint import pp, pprint
from log import Log

class ExceptionDemo:
    __url = 'https://60e1a9ca5a5596001730f1a6.mockapi.io/human'
    
    def get_by_id(self, id):
        data = {} 
        log_server = Log('vhung')
        try:
            check_int = isinstance(id, int)
            print(check_int)
            if not check_int:
                raise TypeError
            response = requests.get(f"{self.__url}/{id}")
            data = response.json()
            if data == 'Not found':
                raise Exception 
        except TypeError:
            log_server.log('ERROR', 'id khong phai kieu int!')
            print('id khong phai kieu int!')         
        except:
            log_server.log('ERROR', 'Server khong tra ve du lieu!')
            print('Server khong tra ve du lieu!')
            
        return data

    def post(self, post_data):
        log_server = Log('vhung')
        try:
            name = post_data['name']
            age = post_data['age']
            response = requests.post(self.__url, data = post_data)
            if response.status_code != 201:
                raise ValueError
            log_server.log('Info','Send thanh cong')
        except ValueError:
            print('gui du lieu khong thanh cong')
            log_server.log('Error','Loi gui du lieu')
        except:
            print('Khong du truong name va age')
            log_server.log('Error','Khong du truong')
        
if __name__ == '__main__':
    ex = ExceptionDemo()
    ex.get_by_id(10)
    
    post_data = {
        "name1": "vhung",
        "age": 99,
    }
