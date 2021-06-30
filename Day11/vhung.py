import os

class JsonFile:
    def __init__(self):
        self.path = path
    
    def show(self, path):
        f = open(path, 'r')
        for line in f:
            print(line)

if __name__ == '__main__':
    path = f'{os.getcwd()}/Day11/data/data.txt'
    json = JsonFile()
    json.show(path)