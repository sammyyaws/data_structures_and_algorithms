class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return
        current=self.head
        while( current.next):
            current=current.next
        current.next=newNode
    def delete_first(self):
         if not self.head:
             return
         self.head=self.head.next
    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head=None
            return
        current=self.head
        while current.next.next:
            current=current.next
        current.next=None
    def showlist(self):
        current=self.head
        while (current.next):
            
            current=current.next
            print(current.data)
        
staffList=SingleList()
studentList=SingleList()
FarmersList=SingleList()

staffList.insert("James")
staffList.insert("kofi")
staffList.insert("Ama")
staffList.insert("Ewuraba")
staffList.showlist()