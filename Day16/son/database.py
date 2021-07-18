#pip install mysql-connector-python
import mysql.connector

class Database:
    def __init__(self):
        # database la schema
        self.myconn = mysql.connector.connect(host = "127.0.0.1", 
                                            user = "root", 
                                            passwd = "123456", 
                                            database = "leadplus")
    
   
        #tạo đối tượng cursor
        self.cur = self.myconn.cursor()
    
    def get_customer(self, id=None):
        if id == None:
            # select dữ liệu từ database
            self.cur.execute("SELECT * FROM customers")
                
            # tìm nạp các hàng từ đối tượng con trỏ  
            result = self.cur.fetchall()
        
        return result

if __name__ == "__main__":
    db = Database()
    customers = db.get_customer()

    for customer in customers:
        print(customer) 