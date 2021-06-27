class CongDan:
    def __init__(self, __name, __id):
        self.name = __name
        self.id = __id
    def get_name(self, name):
        self.name = name

    def get_id(self, id):
        self.id = id

if __name__ == "__main__":
    name = "Nguyen Anh"
    id = '123456763'
    ok_ok = CongDan(name, id)
    print(ok_ok)
