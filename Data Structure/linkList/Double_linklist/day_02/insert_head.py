
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.prev = None

# time complexity O(1)
def insert_at_head(head,tail,value):
    newNode = Node(value)
    if head is None:
        head = newNode
        tail = newNode
        return head,tail
    
    newNode.next = head
    head.prev = newNode
    head = newNode
    
    return head,tail

# time complexity --- O(1)
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


def linklist_length(head):
    count = 0
    temp = head
    while temp is not None:
        count +=1
        temp = temp.next
    return count

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
    head , tail = insert_at_tail(head,tail,value)

head,tail = insert_at_head(head,tail,500)
        
print_normalway(head)
print_reverseway(tail)