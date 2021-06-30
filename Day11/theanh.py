import os
class JsonFile:
    def __init__(self):
        pass
    def show(self, path):           
        f = open(path, 'r')
        for line in f:
            print(line)

if __name__ == '__main__':
    json = JsonFile()
    path = f"{os.getcwd()}/Day11/data/data.txt"
    json.show(path)