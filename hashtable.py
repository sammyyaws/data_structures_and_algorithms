class Hashtable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]
        
    def hashfunction(self,key):
        return sum(ord(c) for c in key)% self.size
    def insert(self,key,value):
        index=self.hashfunction(key)
        bucket=self.table[index]
        
        for i,(k,v) in enumerate(bucket):
            if k==key:
                bucket[i]=(key,value)
                return
        bucket.append((key,value))
        
    #getting the value store with it key 
    def get(self,key):
        index=self.hashfunction(key)
        bucket=self.table[index]
        
        for k,v in bucket:
            if k==key:
                return v
        return None
    #deleting an item in the table
    def delete(self,key):
        index=self.hashfunction(key)
        bucket=self.table[index]
        
        for i,(k,v) in enumerate(bucket):
            if k==key:
                del bucket[i]
                return("Deleted item succesfuly")
        return("item not found")
    # display content of table
    
    def display(self):
        for i,bucket in enumerate(self.table):
            print(i,":",bucket)
            
            
ht=Hashtable(30)
ht.insert("cat","Cathering Ama Jane")
ht.insert('dd',"DanielDorman")
ht.insert("dog","Daniel Oppon Gergi")
ht.insert("sh","sehila harundafada")
ht.insert("kos","kelson owuo sentback")
ht.insert("god","greatest of dudes")


show=ht.display()
print(show)
print(ht.get("dog"))