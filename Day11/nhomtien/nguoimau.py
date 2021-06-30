class NguoiMau():
    def __init__(self,age,money,year,interest):
        self.age = age
        self.money = int(money)
        self.interest = int(interest)
        self.year = int(year)
    
    def say_hi(self):
        print(f'naam nay em {self.age} ngon hong')
    def tinh_lai_kep(self):
        print(f'so tien lai la {self.money}*{self.year}/{self.interest}')