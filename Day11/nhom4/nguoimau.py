from kieunu import KieuNu


class NguoiMau(KieuNu):

    def __init__(self, name, height, weight, age):
        super().__init__(name, height, weight)
        self.__age = age

    def say_hi(self):
        super().say_hi()
        print(f"Tuoi la {self.__age}")

    def tinh_lai_kep(self, money, years, interest):
        money_out = money*((interest/100 + 1)**years)
        print(f"voi so von {money} va lai suat {interest}, sau {years} ban co {money_out}")