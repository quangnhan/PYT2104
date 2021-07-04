import os
import csv
import pandas
import PyPDF2


class JsonFile():

    def __init__(self):
        pass

    def show(self, path):
        with open(path, 'r') as json_file:
            print(json_file.read())


class CSVFile():

    def __init__(self):
        pass

    def show(self, path):
        with open(path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                print(row)


class ExcelFile():
    
    def __init__(self):
        pass

    def show(sellf, path):
        with pandas.ExcelFile(path) as excel_file:
            print(pandas.read_excel(excel_file, sheet_name="Sheet1"))


class PDFFile():
    
    def __init__(self):
        pass

    def show(self, path):
        with open(path, 'rb') as pdf_file:
            reader = PyPDF2.PdfFileReader(pdf_file)
            pdf_data = reader.getPage(0)
            print(pdf_data.extractText())


class File():
    
    def __init__(self, path):
        self.path = path
        file_type = path.split('.')[1]

        if file_type == "txt":
            self.file = JsonFile()
        elif file_type == "csv":
            self.file = CSVFile()
        elif file_type == "xlsx":
            self.file = ExcelFile()
        elif file_type == "pdf":
            self.file = PDFFile()

    def show(self):
        self.file.show(self.path)


# if __name__ == "__main__":
#     path = f"{os.getcwd()}/Day11/data/data.pdf"
    
#     file = File(path)
#     file.show()