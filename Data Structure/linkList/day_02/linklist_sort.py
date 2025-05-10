
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

def sort_linkList(head):
    temp = head
    while temp is not None:
        temp2 = temp.next
        while temp2 is not None:
            
            if temp.value > temp2.value:
                # value swap
                temp.value, temp2.value = temp2.value, temp.value
            temp2 = temp2.next
        temp = temp.next
    
    
def print_linklist_normalway(head):
    temp = head 
    while temp is not None:
        print(temp.value,end=" ")
        temp = temp.next
    print()

head = None
linkList = list(map(int,input().split()))

for value in linkList:
    if value == -1:
        break
    head = insert_at_tail(head,value)

sort_linkList(head)
print_linklist_normalway(head)