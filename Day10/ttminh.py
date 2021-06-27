from server import Server

class KhachHangMoMo:
    account_balance = 50000

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def money_free_for_open_account(self):
        server = Server()
        isLoginSuccess = server.login(self.username, self.password)
        
        if isLoginSuccess:
            print("Login thanh cong!")
        else:
            print("Ban chua co tai khoan, hay tao tai khoan moi")
            username = input('Nhap username: ')
            password = input('Nhap password: ')

            new_customer = KhachHangMoMo(username, password)
            print("Ban da tao tai khoan moi thanh cong")
            print(f"Tai khoan moi co username: {self.username}, password: {self.password}")

    def with_draw(self, amount):
        if amount > self.account_balance:
            print(f"So du trong tai khoan khong du. So du {self.account_balance}")
        else:
            print(f"Ban da rut so tien {amount}")
            print(f"So du con lai la: {self.account_balance}")

if __name__ == "__main__":
    customer = KhachHangMoMo("Minh", "123")
    money_free_for_open_account()
    
    amount = input("Nhap so tien can rut: ")
    with_draw(amount)