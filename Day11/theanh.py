# import os
# class JsonFile:
#     def __init__(self):
#         pass
#     def show(self, path):           
#         f = open(path, 'r')
#         for i in f:
#             print(i)

# if __name__ == '__main__':
#     json = JsonFile()
#     path = f"{os.getcwd()}/Day11/data/data.txt"
#     json.show(path)
import os
import csv
class JsonFile():
    def __init__(self, path):
        self.path = path
    def show(self):
        f = open(self.path,'r')
        for i in f:
            print(i)
class CsvFile():
    def __init__(self, path1):
        self.path1 = path1
    def show(self):
        reader = csv.DictReader(open(self.path1))
        for i in reader:
            print(i)
if __name__ == "__main__":
    path = f"{os.getcwd()}/Day11/data/data.txt"
    path1 = f"{os.getcwd()}/Day11/data/data.csv"
    a = JsonFile(path).show()
    b = CsvFile(path1).show()