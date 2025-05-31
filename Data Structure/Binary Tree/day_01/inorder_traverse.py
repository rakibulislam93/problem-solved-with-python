
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root):
    if root is None: return
    
    inorder(root.left)
    print(root.value,end=" ")
    inorder(root.right)


root = Node(10)
a = Node(20)
b = Node(30)
c = Node(40)
d = Node(50)
e = Node(60)
f = Node(70)

# connection 
root.left = a 
root.right = b 
a.left = c 
a.right = d 
b.left = e 
b.right = f 

inorder(root)