import os
import csv
import pandas as pd


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
        # with open(path,'rt') as f:
        #     data = csv.reader(f)
        #     for row in data:
        #         print(row)
        
        csv_reader = csv.DictReader(open(path), delimiter = ',')
        for i in csv_reader:
            print(i)
            
class XlsxFile:
    def __init__(self):
        pass
    
    def show(self, path):
        pandas_reader = pd.read_excel(path, engine = "openpyxl")
        print(pandas_reader['Name'][0])
        
class File:
    def __init__(self, path):
        file_type = path.split('.')[1]
        self.path = path
        print(file_type)
        if file_type == 'txt':
            self.file = JsonFile()   
        elif file_type == 'csv':
            self.file = CSVFile()
        elif file_type == 'xlsx':
            self.file = XlsxFile()
        
    def show(self):
        self.file.show(self.path)
    
if __name__ == '__main__':
    txt_path = f'{os.getcwd()}/Day11/data/data.txt'
    csv_path = f'{os.getcwd()}/Day11/data/data.csv'
    xlsx_path = f'{os.getcwd()}/Day11/data/data.xlsx'
    file = File(xlsx_path)
    file.show()