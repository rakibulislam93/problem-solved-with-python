
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

a.next = b
b.next = c
c.next = d

print(a.data)
print(a.next.data)
print(a.next.next.data)
print(a.next.next.next.data)
print(a.next.next.next.next) # aikhane None pawa jabe....