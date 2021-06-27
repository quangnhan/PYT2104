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
        return self.__name

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

class CongAn(CongDan):
    def __init__(self, name, id, cap_bac):
        super().__init__(name, id)
        self.__cap_bac = cap_bac

    def get_cap_bac(self):
        return self.__cap_bac

class BacSy(CongDan):
    def __init__(self, name, id, chuyen_khoa):
        super().__init__(name, id)
        self.__chuyen_khoa = chuyen_khoa

    def get_chuyen_khoa(self):
        return self.__chuyen_khoa

    def get_name_and_id(self):
        return {
            "name":self.get_name(),
            "id":self.get_id(),
            "chuyen_khoa": self.__chuyen_khoa
        }

if __name__=='__main__':
    cong_an = CongAn("Duc","1234", "Dai tuong")
    name = cong_an.get_name()
    id = cong_an.get_id()
    cap_bac = cong_an.get_cap_bac()
    bac_si = BacSy("Duc","1234", "Khoa Noi")
    bacsi = bac_si.get_name_and_id()
    print(name,id, cap_bac)
    print(bacsi)