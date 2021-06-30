from kieunu import KieuNu
class NguoiMau(KieuNu):
    def __init__(self, name, height, weight, age):
        super().__init__(name, height, weight)
        self.__age = age
        
    def say_hi(self):
        return super().say_hi()
    
    def tinh_lai_kep(self, money, years, interest):
        lai_kep = money*(1 + interest)**years
        return lai_kep