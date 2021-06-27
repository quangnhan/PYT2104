from Day10.server import Server
class KhachHangMoMo :
    def _init_(KH, username, password ):
        KH.username = username
        KH.password = password
        KH.acccount=0
    def money_tree_for_account(KH):
        server =Server()
        nta = server .login(KH.username, KH.password)
        if nta ["login"] == True:
            KH.account =nta.account
        else :
            KH.nta =50000
    def with_draw(KH,money):
        if money > KH.account.account :
            print(f"{money} there is ")
        else:
            return money
if __name__ == "_main_":
    username = "anh"
    password = "123456"
