# Day 11 cua toi
class JsonFile():
    def __init__(self):
        pass
    def show(self):
        path = f"{os.getcwd()}/Day11/data/data.txt"
        f = open(path,'r')
        return f.readlines()