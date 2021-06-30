import csv

with open("C:\\Users\\Pavilion\\Documents\\PYT2104\Day11\\data\\data.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Index 1 {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} index 2 {row[1]} 22222 {row[2]}.')
            line_count += 1
    print(f'index  {row[2]} 3.')

# Day 11 cua toi
# import os
# class JsonFile():
#     def __init__(self):
#         pass
        
        
#     def show(self,path):
#         self.path = path
#         # path = f"{os.getcwd()}/Day11/data/data.txt"
#         f = open(path,'r')
#         for line in f:
#             return line
# if __name__ == "__main__":  
#     path = f"{os.getcwd()}/Day11/data/data.txt"          
#     json = JsonFile()
#     print(json.show(path))