from database import Database


class Server:
    __db = Database()
    __login = False

    def __init__(self, username, password):
        self.__login = self.__db.login(username, password)

    def get_customer(self, id=None):
        if self.__login:
            print("Login thanh cong!")
            return self.__db.get_customer(id)

        print("Login Error")
