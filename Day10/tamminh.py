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

class CongAn(CongDan):
    def __init__(self, name, id, cap_bac):
        super().__init__(name, id)
        self.__cap_bac = cap_bac

    def get_cap_bac(self):
        return self.__cap_bac

class Bacsi(CongDan):
    def __init__(self, name, id, chuyen_khoa):
        super().__init__(name, id)
        self.__chuyen_khoa = chuyen_khoa
    
    def get_chuyen_khoa(self):
        return self.__chuyen_khoa

    def get_name_and_id(self):
        return {
            "name": self.get_name(),
            "id": self.get_id()
        }

if __name__ == "__main__":
    bs = Bacsi("Minh", "123", "abc")
    print(bs.get_chuyen_khoa())
    print(bs.get_name_and_id())