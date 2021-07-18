from server import Server

if __name__ == "__main__":
    username = "admin"
    password = "admin"
    sv = Server(username, password)
    customers = sv.getCustomer()
    print(customers)