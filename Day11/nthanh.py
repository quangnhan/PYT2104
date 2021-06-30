# import os

# class JsonFile:

#     def __init__(self):
#         pass

#     def show(self,path):
#         f = open(path, 'r')
#         for line in f:
#             print(line)

# if __name__ == '__main__':
#     path = f'{os.getcwd()}/Day11/data/data.txt'
#     json = JsonFile()
#     json.show(path)

import csv
import os

class CsvFile:
    def __init__(self):
        pass

    def show(self,path):
        f = open(path,'rt')
        for row in f:
                print(row)

if __name__ == '__main__':
    path = f'{os.getcwd()}/Day11/data/data.csv'
    csv = CsvFile()
    csv.show(path)
