from dababase import Database

class Server:
    __db = Database()
    __login = False

    def __init__(self, username, password):
        user = self.__db.get_user(username, password)
        self.__login = len(user) == 1

    def get_customer(self, id=None):
        if self.__login:
            return self.__db.get_customer(id)
        
        print("Login Error")

if __name__ == "__main__":
    username = "admin"
    password = "admin"
    sv = Server(username, password)
    print(sv.get_customer())

