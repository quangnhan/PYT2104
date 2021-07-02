
class CaSi:
    def __init__(self,  nguoi_yeu):
        self.nguoi_yeu = nguoi_yeu
    
    def say_hi(self):
        print (f"{self.nguoi_yeu}")
    
    def tha_thinh(self):
        if self.nguoi_yeu == False:
            print('like')
        else:
            print('dislike')