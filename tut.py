class Node :
    def __init__  (self,data):
       self.data=data
       self.next=None
       
class singlyList:
    def __init__(self):
        self.head=None
        #inserting a new node
    def insert(self,data):
        newNode=Node(data)
        
        if not self.head:
            self.head=newNode
            
        current=self.head
        
        while current.next:
                 current=current.next