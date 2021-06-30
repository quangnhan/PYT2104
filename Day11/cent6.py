class JsonFile:
     def __init__(self, path):
         self.path = path
    def show(self):
        f= open (self.path,'r')
        for line in f:
            print (line)
 
 if __name__== "__main__":
     path = f'{os.getcwd()}/Day11/data/data.txt'
    json = JsonFile(path)
    json.show()