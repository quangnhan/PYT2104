
from server import Server
# class KhachHangMoMo:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.account_balance = 0
#     def money_free_for_open_account(self):
#         server = Server()
#         LoginSuccess = server.login(self.username, self.password)
#         if LoginSuccess = True:
#             print("Login thanh cong!")
#             self.account_balance = account_balance
#         else:
#             self.account_balance +=50
#             print("So du hien tai:"{self.account_balance})
#     def with_draw(self, amount):
#         if (amount > self.account_balance):
#             print ("Lỗi")

class CongDan:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    def get_name (self):
        return self.__name
    def get_id (self):
        return self.__id
    def set_name (self, name):
        self.__name = name
    def set_id (self, name):
        self.__id = id

class CongAn(CongDan):
    def __init__(self, name, id, cap_bac):
       super().__init__(name, id)
       self.cap_bac = cap_bac
    def get_cap_bac(self):
        return self.cap_bac

class Bacsi(CongDan):
    def __init__(self, name, id, chuyen_khoa):
       super().__init__(name, id)
       self.chuyen_khoa = chuyen_khoa
    def get_chuyen_khoa(self):
        return self.chuyen_khoa
    def get_name_and_id(self):
        return {
            "name" : self.get_name(),
            "id" : self.get_id()
        }

if __name__ == "__main__":
    name = "Thao"
    id = "1234"
    Thao = CongDan(name, id)
    bacsi = Bacsi(name, id, 'Răng')
    print(bacsi.get_chuyen_khoa())
    print(bacsi.get_name_and_id())

