from server import Server

class KhachHangMoMo:
    def __init__(self,username, password):
        self.username = username
        self.password = password 
        self.acount_balance = 0

    def money_free_for_open_account(self):
        server = Server()
        response = server.login(self.username,self.password)

        if response["login"] == False:
            print("ban chua co tai khoan")
            self.acount_balance = 50




    def with_draw(self, amount):
        pass
