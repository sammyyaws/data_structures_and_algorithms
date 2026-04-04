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
            return
        current=self.head
        #traverse to the end of the list
        while current.next:
             current=current.next
        current.next=newNode
        
    def display(self):
         current=self.head
         while current:
           print(current.data)
           current=current.next
           
           
#creating a new list
students=singlyList()

students.insert("john")
students.insert("doe")
students.insert("smith")
students.display()