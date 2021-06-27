from server import Server

class KhachHangMoMo:
    def __init__(self,username, password):
        self.username = username
        self.password = password 
        self.__acount_balance = 0

    def money_free_for_open_account(self):
        server = Server()
        response = server.login(self.username,self.password)

        if response["login"] == False:
            self.acount_balance = 50000
        else:
            self.__account_balance = server.__account_balance

    def with_draw(self, amount):
        if amount > self.__account_balance:
            print("Your input money is large than your money in account")
            return 0
        else:
            return amount

if __name__=='__main__':
    username = input("Nhap username:")
    password = input("Nhap password:")
    amount = input("Nhap so tien:")
    khach_hang = KhachHangMoMo(username, password, amount)
    khach_hang.money_free_for_open_account()
    khach_hang.with_draw()
