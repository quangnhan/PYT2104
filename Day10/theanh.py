
class CongDan:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    def get_name (self):
        return self.__name
    def get_id (self):
        return self.__id
    def set_name (self, name):
        self.__name = name
    def set_id (self, name):
        self.__id = id

class CongAn(CongDan):
    def __init__(self, name, id, cap_bac):
       super().__init__(name, id)
       self.cap_bac = cap_bac
    def get_cap_bac(self):
        return self.cap_bac

class Bacsi(CongDan):
    def __init__(self, name, id, chuyen_khoa):
       super().__init__(name, id)
       self.chuyen_khoa = chuyen_khoa
    def get_chuyen_khoa(self):
        return self.chuyen_khoa
    def get_name_and_id(self):
        return {
            "name" : self.get_name(),
            "id" : self.get_id()
        }

if __name__ == "__main__":
    name = "The Anh"
    id = "123456"
    Thao = CongDan(name, id)
    bacsi = Bacsi(name, id, 'tai mui hong')
    print(bacsi.get_chuyen_khoa())
    print(bacsi.get_name_and_id())

