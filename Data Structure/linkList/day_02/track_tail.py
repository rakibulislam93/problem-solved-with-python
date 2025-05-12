

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# insert value O(1) time 
def insert_at_tail(head,tail,value):
    newNode = Node(value)
    if head is None:
        head = newNode
        tail = newNode
        return head,tail
    
    tail.next = newNode
    tail = newNode
    
    return head,tail

def print_linklist(head):
    temp = head
    while temp is not None:
        print(temp.value,end=' ')
        temp = temp.next 
    print()
    

head = None
tail = None

linklist = list(map(int,input().split()))
for value in linklist:
    if value == -1:
        break
    head,tail = insert_at_tail(head,tail,value)

print_linklist(head)
