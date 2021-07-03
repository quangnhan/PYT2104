import os
import pandas as pd
import openpyxl
import pprint
import PyPDF2


class JsonFile:

    def __init__(self):
        pass

    def show(self,path):
        f = open(path, 'r')
        for line in f:
            print(line)

class CsvFile:
    def __init__(self):
        pass

    def show(self,path):
        f = open(path,'rt')
        for i in f:
                print(i)

class ExcelFile:

    def __init__(self):
        pass

    def show(self,path):
        f = pd.ExcelFile(path)
        df = pd.read_excel(f, 0, header=None)
        print(df.head())

class ExcelFileX:

    def __init__(self):
        pass

    def show(self,path):
        f = openpyxl.load_workbook(path)
        sheet = f['Sheet1']
        g_all = sheet.values
        pprint.pprint(list(g_all), width=40)

class PdfFile:
    def __init__(self):
        pass

    def show(self,path):
        f = open(path,'rb')
        pdfReader = PyPDF2.PdfFileReader(f)
        print(pdfReader.numPages)
        pageObj = pdfReader.getPage(0)
        print(pageObj.extractText())
        f.close


class File():
    def __init__(self,path):
        self.path = path
        file_type = path.split('.')[1]
        print(file_type)

        if file_type == "txt":
            self.file = JsonFile()
        if file_type == "csv":
            self.file = CsvFile()
        if file_type == "xls":
            self.file = ExcelFile()
        if file_type == "xlsx":
            self.file = ExcelFileX()
        if file_type == "pdf":
            self.file = PdfFile()

    def show(self):
        self.file.show(self.path)

if __name__ == '__main__':
    path = f'{os.getcwd()}/Day11/data/data.xlsx'
    file = File(path)
    file.show()

    # cv = f'{os.getcwd()}/Day11/data/data.csv'
    # csv = CsvFile()
    # csv.show(cv)






    



