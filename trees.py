class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
        def __init__(self):
            self.root=None
        def insert(self,data):
          self.root=self.inInsert(self.root,data)
        def inInsert(self,root,data):
            if root is None:
                return Node(data)
            if data<root.data:
                root.left=self.inInsert(root.left,data)
            else:
                root.right=self.inInsert(root.right,data)
            return root
        def inorder(self,root):
            if root:
             self.inorder(root.left)
             print(root.data)
             self.inorder(root.right)
        def preorder(self,root):
            if root:
                print(root.data)
                self.preorder(root.left)
                self.preorder(root.right)
        def postorder(self,root):
            if root:
                self.postorder(root.left)
                self.postorder(root.right)
                print(root.data)
        def Binsearch(self,root,key):
            if root is None:
                return
            if root.data==key:
                return True
            if key<root.data:
                return self.Binsearch(root.left,key)
            else:
                return self.Binsearch(root.right,key)
        # find the minimum item 
        def findMin(self,root):
            if root is None:
                return None
            while root.left:
                root=root.left
            return root
        
        #find the maximum item
        def findMax(self,root):
            if root is None:
                return None
            while root.right:
                root=root.right
            return root
        def delete(self,root,key):
            if root is None:
                return None
            if key<root.data:
                root.left=self.delete(root.left,key)
            if key>root.data:
                root.right=self.delete(root.rigth,key)
            else:  #case where the  node is a leave node
                 if  root.left and root.right is None:
                    return None
                #the case of having a node that is having only one child
                 if root.left is None:
                     return root.right
                 if root.right is None:
                      return root.left
                 #case of node 2 childreen
                 if root.left and root.right is not None:
                     successor=self.findMin(root.right)
                     root.data=successor.data
                     root.right=self.delete(root.right,successor.data)
            
num=tree()
num.insert(10)
num.insert(5)

num.insert(15)
num.insert(3)       
num.insert(7)
num.insert(12)
num.insert(18)
# num.inorder(num.root)
# print("preorder")
# num.preorder(num.root)
# print("postorder")
# num.postorder(num.root)
print(num.Binsearch(num.root,7))

