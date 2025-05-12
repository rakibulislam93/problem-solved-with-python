
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


head = None
tail = None

linklist = list(map(int,input().split()))
for value in linklist:
    if value == -1:
        break
    head,tail = insert_at_tail(head,tail,value)

print_linklist_normalway(head)
print_linklist_reverseway(tail)