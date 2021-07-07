from server import Server
from gmail import Gmail
from pprint import pprint


if __name__ == "__main__":
    # test server
    url = "https://60e1aaa95a5596001730f1c1.mockapi.io/human"
    server = Server(url)
    id = 5

    data_post = {
        "name": "Minh",
        "email": "tatamminh151196@gmail.com"
    }

    data_put = {
        "name": "test_put",
        "email": "test_put@gmail.com"
    }

    pprint(server.get())
    # pprint(server.get_by_id(7))
    # server.post(data_post)
    # server.put(6, data_put)
    # server.detele(5)

    # test mail
    gmail = Gmail()
    gmail.congratulation()
