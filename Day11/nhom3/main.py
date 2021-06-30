from casi import CaSi
from kieunu import KieuNu
from nguoimau import NguoiMau
from hoahau_ver2 import HoaHau

if __name__ == '__main__':
    cs = CaSi('Ha', '150', '54', True)
    cs.say_hi()
    cs.tha_thinh()
    
    nm = NguoiMau('Van', '145', '43', '20')
    print('Tinh lai kep: ', nm.tinh_lai_kep(100, 2, 0.1))
    
    hh = HoaHau('Kieu', '165', '48')    
    print('Kiem tra so nguyen to:', hh.check_snt(7))