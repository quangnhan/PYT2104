class CongDan:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

if __name__ == "__main__":
    # name = "Nguyen Anh"
    # id = '123456763'
    ok_ok = CongDan("Nguyen Anh", "1231432")
    ten = ok_ok.get_name()
    ma_so = ok_ok.get_id()
    print(ten,ma_so)
