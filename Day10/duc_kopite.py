from server import Server
import os
serve = Server()
class KhachHangMoMo:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def money_free_for_open_account(self):
        path = f"{os.getcwd()}/customers.txt"
        f = open(path, 'w')
        customer = serve.login(self.username, self.password)
        if customer["login"] == False:
            acc = str([self.username, self.password, 50000])
            f.write(acc)

if __name__=='__main__':
    username = input("Nhap username:")
    password = input("Nhap password:")
    khach_hang = KhachHangMoMo(username, password)
    khach_hang.money_free_for_open_account()