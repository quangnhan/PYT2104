from server import Server

# class KhachHangMoMo:
#     def __init__(self,username,passwork):
#         self.username = username
#         self.passwork = passwork
#         self.__account_balance = 0
#     def money_free_for_open_account(self):
#         if
#     def with_draw_amount(self):
#         pass
class CongDan:
    def __init__(self,name,id):
        self.__name = name
        self.__id = id

    def get_name(self):
        self.__name = name

    def get_id(self):
        self.__id = id

    def say_hi(self):
        print(f"{self.__name}co id la {self.__id}")
if __name__ == "__main__":
    name = "tien"
    id = "08"
    tien = CongDan(name,id)

    tien.say_hi()
    print(get.id())

# if __name__ == "__main__":
#     username = "quangnhan"
#     password = "123"
#     server = Server()
#     resposne = server.login(username, password)
#     print(resposne)

