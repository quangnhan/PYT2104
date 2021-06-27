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
    name = "Minh"
    id = "1234567896"
    cd = CongDan(name, id)

    print(cd.get_name())
    print(cd.get_id())

    new_name = cd.set_name("Tam Minh")
    new_id = cd.set_id("987654321")