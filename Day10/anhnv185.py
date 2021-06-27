from server import Server


from server import * 
class KhachHangMoMo:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0

    def money_free_for_open_account():
        server = Server()
        resposne = server.login(username, password)
        if resposne['login'] == "true":
            print("Dang nhap thanh cong")
        else:
            customer_new = []
            customer_new.append[0] = username
            customer_new.append[1] = password
            customer_new.append[2] = 5000
            print("new account")

    def with_draw(self, amount):
        amount = float(input('Xin moi nhap so tien muon rut: '))
        if amount >= self.balance:
            print(f"So tien {amount} ban rut vuot qua so du tai khoan, vui long thu lai ")
        else:
            return amount

if __name__ == "__main__":
    username = "quangnhan"
    password = "123"
    ok_ok = KhachHangMoMo(username, password)
    print(ok_ok)