from kieunu import KieuNu
from nguoimau import NguoiMau
from casi import CaSi



if __name__ == "__main__":
    kn = KieuNu("Hoo","160","55")
    kn.say_hi()

    age = "20"
    money = 7000
    year = 20
    interest = 10

    tuoinguoi = NguoiMau(age,money,year,interest)
    tuoinguoi.say_hi()
    tuoinguoi.tinh_lai_kep()


    ny = "Hao Hao"
    theanh = CaSi(ny)
    theanh.say_hi()
