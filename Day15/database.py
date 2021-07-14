#pip install mysql-connector-python

import mysql.connector

# database la schema
myconn = mysql.connector.connect(host = "127.0.0.1", 
                                    user = "root", 
                                    passwd = "123456", 
                                    database = "leadplus")
   
#tạo đối tượng cursor
cur = myconn.cursor()
 
# select dữ liệu từ database
cur.execute("SELECT * FROM customers")
    
# tìm nạp các hàng từ đối tượng con trỏ  
result = cur.fetchall()

for x in result:
    print(x); 