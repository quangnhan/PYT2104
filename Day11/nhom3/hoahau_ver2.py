from kieunu import KieuNu
import math

class HoaHau(KieuNu):
    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)

    def say_hi(self):
        return super().say_hi()
    
    def check_snt(self, n):
        ktnt = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n%i == 0:
                ktnt = False
        return ktnt