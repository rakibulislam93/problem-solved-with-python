from collections import deque
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def level_order(root):
    q = deque()
    q.append(root)
    while q:
        node = q[0]
        q.popleft()
        print(node.value,end=' ')
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

root = Node(10)
a = Node(20)
b = Node(30)
c = Node(40)
d = Node(50)
e = Node(60)
f = Node(70)
g = Node(80)
h = Node(90)
i = Node(100)

# tree connection 
root.left = a
root.right = b
a.left = c 
a.right = h 
c.right = e 
h.right = i 
b.right = d
d.left = f 
d.right = g

level_order(root)