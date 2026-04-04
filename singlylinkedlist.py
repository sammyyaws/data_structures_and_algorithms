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
      
      
   def display(self):
      current=self.head
      while current:
         print(f"{current.data}",end="->")
         current=current.next
         
         
   def delete_first(self):
      if not self.head:
         return
      self.head=self.head.next
   def delete_last(self):
      if not self.head:
         return
      if not self.head.next:
         self.head=None
      current=self.head
      while current.next.next:
         current=current.next
      current.next=None
   def del_item(self,key):
       if not self.head:
          return
       if (self.head.data==key):
           return
       current=self.head
       while current.next and current.next.data !=key:
          current=current.next
       if current.next:
          current.next==current.next.next
   def del_at_pos(self,pos):
      if not self.head:
         return
      if pos==0:
         self.head=self.head.next
         return
      current=self.head
      for i in range(pos-1):
         if not current.next:
            print("the position is  out of range")
         current=current.next
      if not current.next:
         print("pos is out of range")
         return
      current.next=current.next.next  
      
studentlist=SingleList() 
n=0
while(n<5):
   StudentName=input("Enter the name of student to add to list")
  
   student={"name":StudentName}
   studentlist.insert(student)
   n+=1
studentlist.display() 
studentlist.delete_first()
print("delete")
studentlist.display()
print("del at pos")
studentlist.del_at_pos(2)
studentlist.display()