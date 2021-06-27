from server import Server


from server import * 
class KhachHangMoMo:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def money_free_for_open_account():
        if resposne == "false":
            path = f"{os.getcwd()}/Day10/customers.txt"
            f = open(path, 'w')
            customers = []
            customers.append[0] = username
            customers.append[1] = password
            customers.append[2] = 50
            return customers

    # def with_draw(amount):
    #     amount = float(input('Xin moi nhap so tien muon rut: '))
    #     if amount >= 

if __name__ == "__main__":
    username = "quangnhan"
    password = "123"
    server = Server()
    resposne = server.login(username, password)
    print(resposne)