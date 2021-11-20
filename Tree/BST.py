class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self,child):
        if self.data is child:
            return 
        else:
            if self.data < child:
                if self.right:
                    self.right.insert(child)
                else:
                    self.right = Node(child)
            elif self.data > child:
                if self.left:
                    self.left.insert(child)
                else:
                    self.left = Node(child)
def inorder(root):
    lst = []
    if root:
        lst += inorder(root.left)
        lst.append(root.data)
        lst += inorder(root.right)
    return lst
def postorder(root):
    lst =[]
    if root:
        lst+=postorder(root.left)
        lst+=postorder(root.right)
        lst.append(root.data)
    return lst   
def preorder(root):
    lst= []
    if root:
        lst.append(root.data)
        lst+=preorder(root.left)        
        lst+=preorder(root.right)
    return lst
def BST(lst):
    root = Node(lst[0])
    for i in lst[1:]:
        root.insert(i)
    return root
if __name__ == "__main__":
    lst = [2,4,78,9,6,4,34,67,8]
    root = BST(lst)
    print("List : ",lst)
    print("Inorder : ",inorder(root))
    
    print("Preorder : ",preorder(root))
    
    print("Postorder : ",postorder(root))
    
