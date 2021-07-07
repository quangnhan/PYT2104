import requests
import os
from datetime import datetime
from pprint import pprint

class Server:
    def __init__(self, url):
        self.__url = url
        
    def get(self):
        response = requests.get(self.__url)
        data = response.json()
        # pprint(data)
        self.log('get')
        return data
        
    def post(self, data_post):
        response = requests.post(self.__url, data = data_post)
        data = response.json()
        print('Da post du lieu: ', data)
        self.log('post')
        
    def put(self, data_put, id):
        response = requests.put(f'{self.__url}/{id}', data = data_put)
        data = response.json()
        print(f'Da put du lieu tai id = {id}')
        self.log('put')
        
    def delete(self, id):
        response = requests.delete(f'{self.__url}/{id}')
        print(f'da xoa du lieu tai id = {id}')
        self.log('delete')
        
    def log(self, method):
        path = f"{os.getcwd()}/Day12/vhung/log.txt"
        date = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        log_msg = f"{method} - {date}\n"

        with open(path, 'a') as log_file:
            log_file.write(log_msg)
    
        
# if __name__ == "__main__":
#     sv = Server("https://60e1a9ca5a5596001730f1a6.mockapi.io/human") 
#     data_post = {
#         'name' : "test_post",
#         'age' : 29
#     }
#     id_put = 1
#     data_put = {
#         'name' : "test_put",
#         'age' : 25
#     }
#     id_delete = 3
    
#     pprint(sv.get())
#     sv.put(data_put, id_put)
#     sv.post(data_post)
#     sv.delete(id_delete)