
from server import Server
class KhachHangMoMo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.account_balance = 0
    def money_free_for_open_account(self):
        server = Server()
        LoginSuccess = server.login(self.username, self.password)
        if LoginSuccess = True:
            print("Login thanh cong!")
            self.account_balance = account_balance
        else:
            self.account_balance +=50
            print("So du hien tai:"{self.account_balance})
    def with_draw(self, amount):
        if (amount > self.account_balance):
            print ("Lỗi")

if __name__ == "__main__":
    name = KhachHangMoMo('Cent', 'nữ')
    name = money_free
