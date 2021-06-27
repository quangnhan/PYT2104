import os
from server import Server

class KhachHangMoMo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
 
    def money_free_for_open_account(username, password):
        path = f"{os.getcwd()}/Day10/customers.txt"
        f = open(path, 'a')
        f.write(username + ',' + password + ',' + '50000' )
        f.close()
    
    # def with_draw(username, password, money):
        
        
        
    
if __name__ == '__main__':
    username = "asd"
    password = "123"
    server = Server()
    resposne = server.login(username, password)
    if resposne['login'] == False:
        print(resposne['login'])
        khach_hang = KhachHangMoMo()
        khach_hang.money_free_for_open_account(username, password)
    # else:
        
    