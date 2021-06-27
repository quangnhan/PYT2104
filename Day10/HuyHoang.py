from server import Server
class KhachHangMoMo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.__account_balance = 0 

    def money_free_for_open_account(sefl):
        server = Server()
        dangnhap = server.login(sefl.username, sefl.password)
        if

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

    def set_name(self, id):
        self.__id = id
