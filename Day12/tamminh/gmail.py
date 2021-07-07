import smtplib, ssl
from server import Server


class Gmail:

    def __init__(self):
        self.__port = 465
        self.__smtp_server = "smtp.gmail.com"
        self.__sender_email = "tatamminh151196@gmail.com"
        self.__password = "jsbtgbbjeypgudys"

    def congratulation(self):
        url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"
        server = Server(url)
        list_candicate = server.get()

        context = ssl.create_default_context()
        
        for candicate in list_candicate:
            name = candicate.get("name")
            email = candicate.get("email")
            message = f"""\
                Subject: Hi {name}!

                This message is sent from Python.
                
                Congratulations for joining us!
                """

            with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:
                server.login(self.__sender_email, self.__password)
                server.sendmail(self.__sender_email, email, message)

        return print("Gui mail thanh cong")
