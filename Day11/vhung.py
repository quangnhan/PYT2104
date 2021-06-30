import os
import csv

class JsonFile:
    def __init__(self):
        pass
    
    def show(self, path):
        f = open(path, 'r')
        for line in f:
            print(line)

class CSVFile:
    def __init__(self):
        pass
    
    def show(self, path):
        with open(path,'rt') as f:
            data = csv.reader(f)
            for row in data:
                print(row)

if __name__ == '__main__':
    path = f'{os.getcwd()}/Day11/data/data.csv'
    json = CSVFile()
    json.show(path)