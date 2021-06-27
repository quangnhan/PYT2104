# from server import Server

# class KhachHangMoMo:
#     def __init__(self,username, password):
#         self.username = username
#         self.password = password 
#         self.__acount_balance = 0

#     def money_free_for_open_account(self):
#         server = Server()
#         response = server.login(self.username,self.password)

#         if response["login"] == False:
#             self.acount_balance = 50000
#         else:
#             self.__account_balance = server.__account_balance

#     def with_draw(self, amount):
#         if amount > self.__account_balance:
#             print("Your input money is large than your money in account")
#             return 0
#         else:
#             return amount

# if __name__=='__main__':
#     username = input("Nhap username:")
#     password = input("Nhap password:")
#     amount = input("Nhap so tien:")
#     khach_hang = KhachHangMoMo(username, password, amount)
#     khach_hang.money_free_for_open_account()
#     khach_hang.with_draw()

class CongDan:
    def __init__(self,name,id):
        self.__name = name
        self.__id = id
        
    
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def set_name(self,name):
        self.__name = name

    def set_id(self,id):
        self.__name = id

class CongAn(CongDan):
    def __init__(self,name,id,cap_bac):
        super().__init__(name,id)
        self.__cap_bac = cap_bac
    
    def get_cap_bac(self):
        return self.__cap_bac
        
class BacSi(CongDan):
    def __init__(self,name,id,chuyenkhoa):
        self.__chuyenkhoa = chuyenkhoa
        super().__init__(name,id)

    def get_chuyen_khoa(self):
        return self.__chuyenkhoa

    def get_name_and_id(self):
        name_id = {"name": self.get_name(),"id":self.get_id()}
        return name_id

if __name__ == "__main__":
    name = "Thanh"
    id = "123456"
    
    capbac = "dân đen"
    chuyenkhoa = "thất nghiệp"
    thanh = BacSi(name,id,chuyenkhoa)
    print(thanh.get_name_and_id())
