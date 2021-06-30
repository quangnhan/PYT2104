from Day11.nhom3.kieunu import KieuNu
class HoaHau(KieuNu):

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def say_hi(self):
        print(f" Hello world, I'm {self.name}")

    def check_snt(self,n):
        pass

