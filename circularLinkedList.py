class Node:
    def __init__(self,data):
       self.data=data
       self.next=None
       
    
    
    
    
    
    
    
    
    
       
class Circularlinked:
    def __init__(self):
        self.head=None
    def insert(self,data):
      newNode=Node(data)
      if not self.head:
          self.head=newNode
          self.head.next=self.head
          return
      current=self.head
      while  current.next!=self.head:
          current=current.next
      current.next=newNode
      current.next=self.head
    