
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

def print_linklist_normalway(head):
    temp = head
    while temp is not None:
        print(temp.value,end=' ')
        temp = temp.next 
    print()

def print_linklist_reverseway(tail):
    temp = tail
    while temp is not None:
        print(temp.value,end=' ')
        temp = temp.prev 
    print()

head = Node(10)
a = Node(20)
b = Node(30)

head.next = a
a.prev = head
a.next = b
b.prev = a
tail = b 

print_linklist_normalway(head)
print_linklist_reverseway(tail)