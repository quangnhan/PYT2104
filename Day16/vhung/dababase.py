#pip install mysql-connector-python
import mysql.connector

class Database:
    def __init__(self):
        # database la schema
        self.myconn = mysql.connector.connect(host = "127.0.0.1", 
                                            user = "unknown", 
                                            passwd = "model.kn2412", 
                                            database = "leadplus")
    
   
        # tao doi tuong cursor
        self.cur = self.myconn.cursor()
    
    def get_customer(self, id=None):
        if id == None:
            # select du lieu tu database
            self.cur.execute("SELECT * FROM customers")
                
            # tim nap cac hang tu doi tuong con tro
            result = self.cur.fetchall()
        
        return result

    def get_user(self, username, password):
        sql = f"SELECT * FROM users \
            WHERE `username`='{username}' \
                AND `password`='{password}'"
        # print(sql)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    # ### Test create table
    # def create_table_test(self):
    #     sql = "CREATE TABLE `test` ( \
    #         `id` int NOT NULL AUTO_INCREMENT, \
    #         `name` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,\
    #         PRIMARY KEY (`id`) \
    #         ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;"
        
    #     self.cur.execute(sql)

# if __name__ == "__main__":
#     db = Database()
#     customers = db.get_customer()
#     # create = db.create_table_test()

#     for customer in customers:
#         print(customer) 