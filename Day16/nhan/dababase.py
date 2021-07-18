#pip install mysql-connector-python
import mysql.connector

class Database:
    def __init__(self):
        # database la schema
        self.myconn = mysql.connector.connect(host = "127.0.0.1", 
                                            user = "root", 
                                            passwd = "123456", 
                                            database = "test")
        #tạo đối tượng cursor
        self.cur = self.myconn.cursor()

        #tao bảng
        self.__create_table_users()
        self.__create_table_customer()
        self.__create_table_company_info()
        self.__create_table_websites()
        self.__create_table_ads()
        self.__create_table_websites_ads()
    
    def get_customer(self, id=None):
        if id == None:
            # select dữ liệu từ database
            self.cur.execute("SELECT * FROM customers")
                
            # tìm nạp các hàng từ đối tượng con trỏ  
            result = self.cur.fetchall()
        return result

    def get_user(self, username, password):
        # select dữ liệu từ database
        self.cur.execute(f"SELECT * FROM users WHERE username='{username}' and password='{password}'")
            
        # tìm nạp các hàng từ đối tượng con trỏ  
        result = self.cur.fetchall()
        return result

    def __create_table_users(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS `users` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `username` VARCHAR(45) NULL,
            `password` VARCHAR(45) NULL,
            PRIMARY KEY (`id`))
            ENGINE = InnoDB
        """)

    def __create_table_customer(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS `customers` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `name` VARCHAR(45) NULL DEFAULT NULL,
            PRIMARY KEY (`id`))
            ENGINE = InnoDB
            AUTO_INCREMENT = 4
            DEFAULT CHARACTER SET = utf8mb4
            COLLATE = utf8mb4_0900_ai_ci
        """)

    def __create_table_company_info(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS `company_info` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `customer_id` INT NOT NULL,
            `ma_so_thue` VARCHAR(45) NULL DEFAULT NULL,
            PRIMARY KEY (`id`, `customer_id`),
            INDEX `fk_comany_info_customers_idx` (`customer_id` ASC) VISIBLE,
            CONSTRAINT `fk_comany_info_customers`
                FOREIGN KEY (`customer_id`)
                REFERENCES `customers` (`id`))
            ENGINE = InnoDB
            AUTO_INCREMENT = 4
            DEFAULT CHARACTER SET = utf8mb4
            COLLATE = utf8mb4_0900_ai_ci
        """)

    def __create_table_websites(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS `websites` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `url` VARCHAR(45) NULL DEFAULT NULL,
            `customer_id` INT NULL DEFAULT NULL,
            PRIMARY KEY (`id`),
            INDEX `fk_site_customer_idx` (`customer_id` ASC) VISIBLE,
            CONSTRAINT `fk_websites_customers`
                FOREIGN KEY (`customer_id`)
                REFERENCES `customers` (`id`))
            ENGINE = InnoDB
            AUTO_INCREMENT = 6
            DEFAULT CHARACTER SET = utf8mb4
            COLLATE = utf8mb4_0900_ai_ci
        """)

    def __create_table_ads(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS `ads` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `name` VARCHAR(45) NULL,
            `price` VARCHAR(45) NULL,
            PRIMARY KEY (`id`))
            ENGINE = InnoDB
        """)

    def __create_table_websites_ads(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS `websites_has_ads` (
            `websites_id` INT NOT NULL,
            `ads_id` INT NOT NULL,
            PRIMARY KEY (`websites_id`, `ads_id`),
            INDEX `fk_websites_has_ads_ads1_idx` (`ads_id` ASC) VISIBLE,
            INDEX `fk_websites_has_ads_websites1_idx` (`websites_id` ASC) VISIBLE,
            CONSTRAINT `fk_websites_has_ads_websites1`
                FOREIGN KEY (`websites_id`)
                REFERENCES `websites` (`id`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
            CONSTRAINT `fk_websites_has_ads_ads1`
                FOREIGN KEY (`ads_id`)
                REFERENCES `ads` (`id`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8mb4
            COLLATE = utf8mb4_0900_ai_ci
        """)

if __name__ == "__main__":
    db = Database()
    # customers = db.get_customer()

    # for customer in customers:
    #     print(customer) 