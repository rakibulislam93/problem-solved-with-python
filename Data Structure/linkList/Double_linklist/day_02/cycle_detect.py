
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
head = Node(10)
a = Node(20)
b = Node(30)
c = Node(40)

head.next = a 
a.next = b 
b.next = c 
c.next = b

slow = head
fast = head
flag = False
while fast and fast.next is not None:
    slow = slow.next
    fast = fast.next.next 
    
    if slow == fast:
        flag = True
        break

print('Cycle detected' if flag else 'No cycle detected...')