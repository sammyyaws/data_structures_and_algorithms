#queues with arrays

class Queue:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self,data):
        self.queue.append(data)
        return
    def dequeue(self):
        if len(self.queue)!=0:
           return self.queue.pop(0)
        return("queue is empty")
    def show(self):
        print(self.queue)
        
# queues with linkedlist    
class Node:
    def __init__(self,data):
      self.data=data
      self.next=None
class Queue:        
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue (self,data):
        newNode=Node(data)
        if self.rear is None:
            self.front=self.rear=newNode
        self.rear.next=newNode
        self.rear=newNode
    def dequeue(self):
        if self.front is None:
            return("the queue is empty")
        currentFront=self.front
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return currentFront
    def display(self):
        current=self.front
        while current.next:
          print(current.data)
          current=current.next
          
gradesq=Queue()
gradesq.enqueue(70)
gradesq.enqueue(60)
gradesq.enqueue(56)
gradesq.enqueue(76)
gradesq.enqueue(0)

gradesq.display()
print("showed list")
gradesq.dequeue()
gradesq.display()
print("dequeued")
gradesq.dequeue()
gradesq.display()