import os
from Day10.server import Server

class KhachHangMoMo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.account_balance = 0
    
    def money_free_for_open_account(self, username, password):
        server = Server()
        resposne = server.login(username, password)
        if resposne['login'] == False:
            self.account_balance = 50000
        else: 
            self.account_balance = resposne['account_balance']
    
    def with_draw(self, money):
        if money > self.account_balance:
            print('Loi!!')
        else: 
            self.account_balance -= money
    
    