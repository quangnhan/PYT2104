import os
class JsonFile():
    def __init__(self, path):
        self.path = path

    def show(self):
        f = open(self.path,'r')
        for i in f:
            print(i)

if __name__ == "__main__":
    path = f"{os.getcwd()}/data/data.txt"
    a = JsonFile(path)
    a.show()
