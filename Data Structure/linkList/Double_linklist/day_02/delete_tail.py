
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
        return head,tail
    tail.next = newNode
    newNode.prev = tail
    tail = newNode
    return head,tail



def delete_tail(head,tail):
    delNode = tail
    if tail is None:
        return head,tail
    if tail.prev is None:
        head = None
        tail = None
    else:
        tail = tail.prev
        tail.next = None
    
    del delNode
    return head,tail
    
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
head,tail = delete_tail(head,tail)
print('*********')
print_normalway(head)
print_reverseway(tail)