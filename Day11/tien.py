# Day 11 cua toi
import os
class JsonFile():
    def __init__(self):
        pass
        
        
    def show(self,path):
        self.path = path
        # path = f"{os.getcwd()}/Day11/data/data.txt"
        f = open(path,'r')
        for line in f:
            return line
if __name__ == "__main__":  
    path = f"{os.getcwd()}/Day11/data/data.txt"          
    json = JsonFile()
    print(json.show(path))