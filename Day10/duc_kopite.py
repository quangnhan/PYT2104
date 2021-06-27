from server import Server

class KhachHangMoMo:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__account_balance = 0

    def money_free_for_open_account(self):
        serve = Server()
        customer = serve.login(self.username, self.password)
        if customer["login"] == False:
            self.__account_balance = 50000
        else:
            self.__account_balance = serve.account_balance

    def with_draw(self, amount):
        if amount > self.__account_balance:
            print("Your input money is large than your money in account")
        else:
            self.__account_balance = self.__account_balance - amount

if __name__=='__main__':
    username = input("Nhap username:")
    password = input("Nhap password:")
    amount = input("Nhap so tien:")
    khach_hang = KhachHangMoMo(username, password)
    khach_hang.money_free_for_open_account()
    khach_hang.with_draw()