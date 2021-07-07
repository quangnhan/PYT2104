import smtplib, ssl
from server import Server

class Email:
    def __init__(self, url):
        self.__port = 465  # For SSL
        self.__smtp_server = "smtp.gmail.com"
        self.__sender_email = "starlight.9389@gmail.com"  # Enter your address
        self.__password = "dytmkwjzveizcvjy"
        self.__url = url
    
    def congratulation(self):
        sv = Server(self.__url)
        list_human = sv.get()
        for human in list_human:
            message = f"""Subject: Hi {human['name']}! This message is sent from vhung."""
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
                server.login(self.__sender_email, self.__password)
                server.sendmail(self.__sender_email, human['email'], message)
        
# if __name__ == "__main__":
#     mail = Email("https://60e1a9ca5a5596001730f1a6.mockapi.io/human") 
#     mail.congratulation()