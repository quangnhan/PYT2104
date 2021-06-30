from kieunu import KieuNu
class CaSi(KieuNu):
    def __init__(self, name, height, weight, nguoi_yeu):
        super().__init__(name, height, weight)
        self.__nguoi_yeu = nguoi_yeu
    
    def say_hi(self):
        return super().say_hi()
    
    def tha_thinh(self):
        if self.__nguoi_yeu == False:
            print('I Love U')
        else:
            print('I Hate U')
