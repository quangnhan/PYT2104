from casi import CaSi
from kieunu import KieuNu
from nguoimau import NguoiMau
from hoahau import HoaHau

if __name__ == '__main__':
    cs = CaSi('Minh', '160', '60', True)
    cs.say_hi()
    cs.tha_thinh()
    
    nm = NguoiMau('Minhhh', '165', '70', '20')
    nm.say_hi()
    nm.tinh_lai_kep(100, 2, 0.1)

    hh = HoaHau('Minhhhhh', '165', '400')
    hh.say_hi()
    hh.check_snt(2)