from kieunu import KieuNu

class HoaHau(KieuNu):

    def __init__(self, name):
        super().__init__(name)

    def say_hi(self):
        return self.say_hi

    def check_snt(n):
        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count += 1
            if count == 2:
                return True
            return False


