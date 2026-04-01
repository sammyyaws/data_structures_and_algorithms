class Node:
  def __init__(self,data):
      self.data=data
      self.next=None 
      self.prev=None


class doublylinked:
  def __init__(self):
    self.head=None
  
  def insert(self,data):
     newNode=Node(data)
     if not self.head:
        self.head=newNode
        return
     current=self.head
     while(current.next):
       current=current.next
     current.next=newNode
     newNode.prev=current
  def display(self):
    current=self.head
    while current:
      print(current.data)
      current=current.next
dou=doublylinked()
dou.insert(10)
dou.insert(565)
dou.insert(645)
dou.display()