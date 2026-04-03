class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self.ininsert(self.root,data)
    def ininsert(self,root,data):
       if root is None:
           return(Node(data))
       if data<root.data:
           root.left=self.ininsert(root.left,data)
       else:
           root.right=self.ininsert(root.right,data)
       return root