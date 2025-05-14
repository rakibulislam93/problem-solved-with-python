
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
def insert_at_tail(head,tail,value):
    newNode = Node(value)
    if head is None:
        head = newNode
        tail = newNode
        return head, tail
    tail.next = newNode
    newNode.prev = tail
    tail = newNode
    return head,tail 

def delete_at_position(head,pos):
    temp = head
    for i in range(pos-1):
        temp = temp.next 
    
    delNode = temp.next 
    temp.next = delNode.next
    delNode.next.prev = temp
    
    del delNode
    return head

def print_normalway(head):
    temp = head
    while temp is not None:
        print(temp.value,end=' ')
        temp = temp.next 
    print()

def print_reverseway(tail):
    temp = tail 
    while temp is not None:
        print(temp.value,end=' ')
        temp = temp.prev 
    print()

head = None
tail = None

linklist = list(map(int,input().split()))
for value in linklist:
    if value == -1:
        break
    head,tail = insert_at_tail(head,tail,value)
    
print_normalway(head)
print_reverseway(tail)

head = delete_at_position(head,2)
print('**********')
print_normalway(head)
print_reverseway(tail)
