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
        return self.__name

    def set_name(self,name):
        self.__name = name

    def set_id(self,id):
        self.__id = id

    def get_id(self):
        return self.__id

    def say_hi(self):
        print(f"{self.__name}co id la {self.__id}")

class CongAn(CongDan):
    def __init__(self,name,id,cap_bac):
        super().__init__(name,id)
        self.__cap_bac = cap_bac
    
    def get_cap_bac(self):
        return self.__cap_bac

class BacSi(CongDan):
    def __init__(self,name,id,chuyen_khoa):
        super().__init__(name,id)
        self.__chuyen_khoa = chuyen_khoa

    def get_chuyen_khoa(self):
        return self.__chuyen_khoa

    def get_name_and_id(self):
        return self.__name,self.__id



if __name__ == "__main__":
    name = "tien"
    id = "08"
    tien = CongDan(name,id)

    tien.say_hi()
    print(tien.get.id())

# if __name__ == "__main__":
#     username = "quangnhan"
#     password = "123"
#     server = Server()
#     resposne = server.login(username, password)
#     print(resposne)

