
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

def insert_at_head(head,pos,value):
    newNode = Node(value)
    
    if pos == 0:
        newNode.next = head
        head.prev = newNode
        head = newNode
        
        return head

def print_linklist(head):
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

head = None
tail = None
linklist = list(map(int,input().split()))
for value in linklist:
    if value == -1:
        break
    head,tail = insert_at_tail(head,tail,value)

print_linklist(head)
head = insert_at_head(head,0,30)
print_linklist(head)
print_linklist_reverseway(tail)