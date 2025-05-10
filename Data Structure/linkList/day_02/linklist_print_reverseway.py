
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

def insert_at_tail(head,value):
    newNode = Node(value)
    if head is None:
        head = newNode
        return head
    temp = head 
    while temp.next is not None:
        temp = temp.next 
    temp.next = newNode
    
    return head

def print_linklist_normalway(head):
    temp = head 
    while temp is not None:
        print(temp.value,end=" ")
        temp = temp.next
    print()

def print_linklist_reverseway(head):
    temp = head
    if temp is None:
        return
    print_linklist_reverseway(temp.next)
    print(temp.value,end=' ')


head = None
linkList = list(map(int,input().split()))

for value in linkList:
    if value == -1:
        break
    head = insert_at_tail(head,value)

print_linklist_normalway(head)
print_linklist_reverseway(head)