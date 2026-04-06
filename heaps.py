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
                self.heap[p]=self.heap[i]
                self.heap[i]=self.heap[p]
                i=p
            else:
                break