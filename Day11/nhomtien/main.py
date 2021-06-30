from kieunu import KieuNu
from nguoimau import NguoiMau



if __name__ == "__main__":
    kn = KieuNu("Hao","160","55")
    print(kn.say_hi())

    age = "20"
    money = 7000
    year = 20
    interest = 10

    tuoinguoi = NguoiMau(age,money,year,interest)
    print(tuoinguoi.say_hi())
    tuoinguoi.tinh_lai_kep()

