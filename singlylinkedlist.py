class Node:
   def __init__(self,data):
      self.data=data
      self.next=None
      
      
class SingleList ():
   def __init__(self):
      self.head=None
   def insert(self,data):
      newNode=Node(data)
      if not self.head:
         self.head=newNode
         return
      current=self.head
      while current.next:
         current=current.next
      current.next=newNode
      
studentlist=SingleList()
n=0
while(n<4):
   StudentName=input("Enter the name of student to add to list")
   Studentcourse=input("enter student's course")
   student={"name":StudentName,"course":Studentcourse}
   studentlist.insert(student)
   n+=1