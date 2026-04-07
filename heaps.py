class MaxHeap:
    def __init__(self):
        self.heap=[]
        
    def parentInd(i):     
        return((i-1)//2)
    
    def leftChildInd(i):
        return (2(i)+1)
    def rightChildInd(i):
        return(2(i)+2)
    
    def insert(self,data):
        self.heap.append(data)
        i=len(self.heap)-1
       
        while i>0:
            p=self.parentInd(i)
            if self.heap[i]>self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i=p
            else:
                break
            
    def deleteroot(self,data):
       if  not self.heap:
           return None
       if len (self.heap)==1:
           self.heap.pop()
       root_value=0
       self.heap[0]=self.heap.pop()
       self.bubbledown(0)
       
    def bubbledown(self,i):
         #check if left item exits
         while True:
            left=self.leftChildInd(i)
            right=self.rightChildInd(i)
            largest=i
            if left<len(self.heap) and self.heap[left]>self.heap[largest]:
               largest=left
            if right<len(self.heap) and self.heap[right]>self.heap[largest]:
               largest=right
            if largest!=i:
                self.heap[i],self.heap[largest]=self.heap[largest],self.heap[i]
                i=largest
            else:
                break
       
       
       
       