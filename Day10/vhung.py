import os
from server import Server

# class KhachHangMoMo:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.__account_balance = 0
    
#     def money_free_for_open_account(self, username, password):
#         server = Server()
#         resposne = server.login(username, password)
#         if resposne['login'] == False:
#             self.__account_balance = 50000
#         else: 
#             self.__account_balance = resposne['account_balance']
    
#     def with_draw(self, money):
#         if money > self.__account_balance:
#             print('Loi!!')
#             return self.__account_balance
#         else: 
#             return money
    
# class CongDan:
#     def __init__(self, name, id):
#         self.__name = name
#         self.__id = id
                
#     def get_name(self):
#         return self.__name
    
#     def get_id(self):
#         return self.__id
    
#     def set_name(self, name):
#         self.__name = name
    
#     def set_id(self, id):
#         self.__id = id
        
# class CongAn(CongDan):
#     def __init__(self, name, id, cap_bac):
#         super().__init__(name, id)
#         self.__cap_bac = cap_bac
    
#     def get_cap_bac(self):
#         return self.__cap_bac
    
class BacSi(CongDan):
    def __init__(self, name, id, chuyen_khoa):
        super().__init__(name, id)
        self.__chuyen_khoa = chuyen_khoa
    
    def get_chuyen_khoa(self):
        return self.__chuyen_khoa
    
    def get_name_and_id(self):
        return {
            'name' : self.get_name(),
            'id' : self.get_id()
        }
        
if __name__ == '__main__':
    name = 'htv'
    id = '123456'
    bs = BacSi(name, id, 'Thu y')
    print(bs.get_chuyen_khoa())
    print(bs.get_name_and_id())
