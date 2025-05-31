
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


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
