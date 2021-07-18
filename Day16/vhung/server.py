from dababase import Database

class Server:
    __db = Database()
    __login = False

    def __init__(self, username, password):
        login = self.__db.get_user(username, password)
        if login != []: 
            print(login)
            self.__login = True
        else: 
            print("Sai ten dang nhap hoac mat khau!!!")

    def getCustomer(self, id=None):
        customers = self.__db.get_customer()
        return customers  

if __name__ == "__main__":
    username = "admin"
    password = "admin1"
    sv = Server(username, password)
    print(sv.getCustomer())