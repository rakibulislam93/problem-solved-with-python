

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

def sort_linklist(head):
    
    temp1 = head
    while temp1.next is not None:
        temp2 = temp1.next
        while temp2 is not None:
            if temp1.value > temp2.value:
                temp2.value,temp1.value = temp1.value,temp2.value
            temp2 = temp2.next 
        temp1 = temp1.next
    
    

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

sort_linklist(head)
print_linklist(head)
