


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

def check_ascending(head):
    flag = True
    temp = head
    while temp.next is not None:
        if temp.value > temp.next.value:
            flag = False
            return flag
        temp = temp.next 
        
    return flag


head = None
linkList = list(map(int,input().split()))

for value in linkList:
    if value == -1:
        break
    head = insert_at_tail(head,value)

if check_ascending(head):
    print('YES')
else:
    print('NO')