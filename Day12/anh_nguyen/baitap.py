# 1) Bài tập về request
# - Viết class Server
# - __url = https://www.mockapi.io/
# - Viết 4 hàm để thực hiện 4 lệnh get, post, put, delete
# - Viết hàm log để lưu log vào file log.txt, Ví dụ:
#     get - 10:20:23 4/7/2021
#     post - 10:20:28 4/7/2021
#     put - 10:20:28 4/7/2021
#     delete - 10:20:50 4/7/2021

# 2) Bài tập về viết email
# - Viết class Gmail
# - Viết hàm congratulation(name, email) để tự động gửi email đến những ứng viên trúng tuyển,
# trong đó danh sách ứng viên lấy từ API (Dùng class Server đã viết ở trên để lấy dữ liệu)
import os
import requests
import pprint
import json
from datetime import datetime
import smtplib, ssl

class Server():
    def __init__(self, url):
        self.__url = url

    def get_url(self):
        response_get = requests.get(self.__url)
        return "GET", response_get.json()

    def post_url(self, name, age):
        self.name = name
        self.age = age
        new_data = {
            "name": f"{name}",
            "age": f"{age}",
            }

        response_post = requests.post(self.__url, data = new_data )
        return response_post.json()

    def put_url(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        new_data = {
            "name": f"{name}",
            "age": f"{age}",
            }

        response_put = requests.put(f"{self.__url}/{self.id}", data = new_data)
        return response_put.json()

    def delete_url(self, id):
        self.id = id
        response_delete = requests.delete(f"{self.__url}/{self.id}")
        return response_delete.json()

    def write_log(self):
        self.log = Server(url).get_url()
        log_path = './Day12/anh_nguyen/logfile'       #Tạo đường dẫn tới thư mục chứa log
        log_filename = 'log.txt'
        time = datetime.now()
        os.makedirs(log_path, exist_ok=True)
        try:
            file = open(os.path.join(log_path,log_filename), 'a+')
            file.write(f'{time.strftime("%H:%M:%S %d-%m-%Y")} - {self.log} \n')
        except PermissionError :
            print("\n Error : Cant open logfile. Please Try again")
            input(">>")
            sys.exit()
        return file

class Gmail(Server):
    def __init__(self, url):
        super().__init__(url)
        list_ =super().get_url()

    def congratulation(self, name, email):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "anh13071996@gmail.com"  # Enter your address
        receiver_email = "anh13071996@gmail.com"  # Enter receiver address
        password = "dhpjcrcqqnczktas"
        message = """\
        Subject: Congratulation

        Congratulation ."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    url = "https://60e1a9545a5596001730f19b.mockapi.io/human"
    get = Server(url).get_url()
    # post = Server(url).post_url("NGuyen Anh", "10")
    log = Server(url).write_log()
    print(get)
    # print(post)
