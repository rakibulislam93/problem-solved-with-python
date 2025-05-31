
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def postorder(root):
    if root is None: return
    postorder(root.left)
    postorder(root.right)
    print(root.value,end=" ")

root = Node(10)
a = Node(20)
b = Node(30)
c = Node(40)
d = Node(50)
e = Node(60)
f = Node(70)
g = Node(80)

# connection 
root.left = a 
root.right = b 
a.left = c 
c.right = d 
d.left = e 
d.right = f
b.right = g 

postorder(root)