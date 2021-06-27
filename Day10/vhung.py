import os

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
#             return 0
#         else: 
#             return self.__account_balance
    
class CongDan:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
                
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        self.__name = name
    
    def set_id(self, id):
        self.__id = id