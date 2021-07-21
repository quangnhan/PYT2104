# pip install mysql-connector-python
import mysql.connector


class Database:

    def __init__(self):
        # database la schema
        self.myconn = mysql.connector.connect(host="127.0.0.1",
                                            user="root",
                                            passwd="123456",
                                            database="minh_mysql")

        # tạo đối tượng cursor
        self.cur = self.myconn.cursor()

    def get_customer(self, id=None):
        if id is None:
            # select dữ liệu từ database
            self.cur.execute("SELECT * FROM customer")

            # tìm nạp các hàng từ đối tượng con trỏ  
            result = self.cur.fetchall()

        return result

    def login(self, username, password):
        sql = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
        self.cur.execute(sql)
        result = self.cur.fetchall()

        return True if result else False
