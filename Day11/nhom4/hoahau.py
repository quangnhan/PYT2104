import math
from kieunu import KieuNu


class HoaHau(KieuNu):

    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)

    def check_snt(self, n):
        if n == 0 or n == 1:
            return print(f"{n} khong la so nguyen to")

        if 1 < n < 4:
            return print(f"{n} la so nguyen to")
        
        if n >= 4:
            sqrt_n = int(math.sqrt(n))

            for i in range(2, sqrt_n):
                if n % i == 0: break
            else:
                return print(f"{n} la so nguyen to")
            
            return print(f"{n} khong la so nguyen to")
