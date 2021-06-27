from server import Server
class KhachHangMoMo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__account_balance = 0 

    def money_free_for_open_account(sefl):
        server = Server()
        dangnhap = server.login(sefl.username, sefl.password)
        

    def with_draw(self, amount):
        pass

class CongDan:
    def __init__(self, name, id):
        self.__name = name
        self.__id = int(id)

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

if __name__=='__main__':
    congdan = CongDan("huyhoang", 1234)
    congdan.set_name("huy")
    congdan.set_id(12)
    name = congdan.get_name()
    id = congdan.get_id()
    print(name, id)

class CongAn(CongDan):
    def __init__(self, name, id, cap_bac):
        super().__init__(name, id, cap_bac)
        self.__cap_bac = cap_bac

    def get_cap_bac(self):
        return self.__cap_bac

class BacSi(CongDan):
    def __init__(self, name, id, chuyen_khoa):
        super().__init__(name, id, chuyen_khoa)
        self.__chuyen_khoa = chuyen_khoa 

    def get_chuyen_khoa(self):
        return self.__chuyen_khoa
    
    def get_name_and_id(self):
        {
            "name" = self.__name
            "id"   = self.__id
        }