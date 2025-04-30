

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

def show_linkList(head):
    temp = head 
    while temp is not None:
        print(temp.value,end=' ')
        temp = temp.next 
    print()


head = None

# while True:
#     value = int(input())
#     if value == -1:
#         break
#     head = insert_at_tail(head,value)

linkList = list(map(int,input().split()))

for value in linkList:
    if value == -1:
        break
    head = insert_at_tail(head,value)

show_linkList(head)