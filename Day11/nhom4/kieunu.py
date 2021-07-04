class KieuNu():

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def say_hi(self):
        print(f"Xin chao tat ca moi nguoi, toi la {self.name}, cao {self.height}, nang {self.weight}")