from kieunu import KieuNu


class CaSi(KieuNu):

    def __init__(self, name, height, weight, nguoi_yeu):
        super().__init__(name, height, weight)
        self.__nguoi_yeu = nguoi_yeu

    def say_hi(self):
        super().say_hi()

    def tha_thinh(self):
        if self.__nguoi_yeu:
            print("Thinh thiu")
        else:
            print("Thinh thom")