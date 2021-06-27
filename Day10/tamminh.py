# from server import Server

# class KhachHangMoMo:

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.__account_balance = 0

#     def money_free_for_open_account(self):
#         server = Server()
#         response = server.login(self.username, self.password)
        
#         if response["login"]:
#             print("Login thanh cong!")
#             self.__account_balance = int(response["account_balance"])
#         else:
#             print("Ban chua co tai khoan, hay tao tai khoan moi")
#             self.__account_balance = 50000

#             print("Ban da tao tai khoan moi thanh cong")
#             print(f"Tai khoan moi co username: {self.username}, password: {self.password}")

#     def with_draw(self, amount):
#         print(self.__account_balance)
#         if amount > self.__account_balance:
#             print(f"So du trong tai khoan khong du. So du {self.__account_balance}")
#         else:
#             print(f"Ban da rut so tien {amount}")
            
#             print(f"So du con lai la: {self.__account_balance - amount}")

# if __name__ == "__main__":
#     customer = KhachHangMoMo("bacho", "1234")

#     customer.money_free_for_open_account()

#     customer.with_draw(2000)

class CongDan:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_name(self):
        return self.__name

    def get_id(self, id):
        return self.__id