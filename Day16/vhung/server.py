from dababase import Database

class Server:
    __db = Database()
    __login = False

    def __init__(self, username, password):
        login = self.__db.get_user(username, password)
        if self.__login != []: 
            print(f"Logined as '{login[0][1]}'")
            self.__login = True
        else: 
            print("Sai ten dang nhap hoac mat khau!!!")

    def getCustomer(self, id=None):
        customers = None
        if self.__login:
            customers = self.__db.get_customer()
        return customers  
