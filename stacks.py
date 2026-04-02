####array implementation of a stack 

class Stack:
    def __init__(self):
        self.stack=[]
    def pop(self):
        if len(self.stack)==0:
            print("stack is empty")
        self.stack.pop()
    def push(self,data):
        self.stack.append(data)
    def peek(self):
        if len(self.stack)==0:
          print ("stack  is empty")
        print(self.stack[-1])
    def display(self):
        print(self.stack)
    
s=Stack()
s.push(80)
s.push(50)
s.push(40)
s.push(30)
s.display()
print(s.peek())


##linked lists
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
  
class Lstack:
    def __init__(self):
        self.top=None
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode
    def pop(self):
        if not self.top:
            return("empty stack")
        removed =self.top.data
        self.top=self.top.next
        print(f"removed{removed}")
        return
    def show(self):
        current=self.top
        while current:
            print(current.data,end="-->>")
            current=current.next
    
name=Lstack()
name.push("Jane") 
name.push("kofi")
name.push("ama")
name.push("kiki")
name.push("Jolar")
name.push("Kobby")
name.push("Leglo")
name.show()   
name.pop()
name.show()