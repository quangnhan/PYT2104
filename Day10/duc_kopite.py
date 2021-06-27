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

class CongDan:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_name(self):
        print(f"Ten cua ban la {self.__name}")
        return self.__name

    def get_id(self):
        print(f"ID cua ban la {self.__id}")
        return self.__id
if __name__=='__main__':
    cong_dan = CongDan("Duc","1234")
    cong_dan.get_name()
    cong_dan.get_id()