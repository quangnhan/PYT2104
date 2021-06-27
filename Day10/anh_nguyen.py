class CongDan:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        
    def get_name(self, name):
        return self.name

    def get_id(self, id):
        return self.id

if __name__ == "__main__":
    name = "Nguyen Anh"
    id = '123456763'
    ok_ok = CongDan(name, id)
    print(ok_ok)
