from server import Server

class KhachHangMoMo:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.account_balance = 0

    def money_free_for_open_account(self):
        server = Server()
        response = server.login(self.username, self.password)
        
        if response["login"]:
            print("Login thanh cong!")
        else:
            print("Ban chua co tai khoan, hay tao tai khoan moi")
            self.account_balance = 50000

            print("Ban da tao tai khoan moi thanh cong")
            print(f"Tai khoan moi co username: {self.username}, password: {self.password}")

    def with_draw(self, amount):
        if amount > self.account_balance:
            print(f"So du trong tai khoan khong du. So du {self.account_balance}")
        else:
            print(f"Ban da rut so tien {amount}")
            print(f"So du con lai la: {self.account_balance - amount}")