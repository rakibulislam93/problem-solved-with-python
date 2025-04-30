

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

def length_linkList(head):
    count = 0
    temp = head
    
    while temp is not None:
        count +=1
        temp = temp.next 
    return count

head = None
linkList = list(map(int,input().split()))

for value in linkList:
    if value == -1:
        break
    head = insert_at_tail(head,value)

print(length_linkList(head))