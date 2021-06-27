import os

class Server:
    def __get_all_customers(self):
        path = f"{os.getcwd()}/Day10/customers.txt"
        f = open(path, 'r')
        customers = []

        for line in f:
            username, password, account_balance = line.split(',')
            customers.append({
                "username": username, 
                "password": password, 
                "account_balance": int(account_balance), 
            })

        return customers

    def login(self, username, password):
        customers = self.__get_all_customers()
        login = False
        account_balance = 0

        for customer in customers:
            if customer["username"] == username and customer["password"] == password:
                login = True
                account_balance = customer["account_balance"]
                break

        return {
            "login" : login,
            "account_balance" : account_balance,
        }

if __name__ == "__main__":
    username = "quangnhan"
    password = "123"
    server = Server()
    resposne = server.login(username, password)
    print(resposne)