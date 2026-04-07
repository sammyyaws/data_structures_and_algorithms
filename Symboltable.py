class SymbolTable:
    def __init__(self):
        self.table={}
    def insert(self,key,value):
        self.table[key]=value
    def search(self,key,value):
        for k,v in enumerate(self.table):
            if k==key:
             return v