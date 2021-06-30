class NguoiMau():
    def __init__(self):
        pass

    def age(self, age, name = "ngoc trinh"):
        self.age = age

    def say_hi(self):
        print(f"{sefl.name}, {sefl.age} tuoi xin chao cac ban")
    
if __name__ == "__main__":
    a = NguoiMau("40").say_hi