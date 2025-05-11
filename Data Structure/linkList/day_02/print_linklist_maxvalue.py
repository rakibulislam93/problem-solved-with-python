
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

def find_linklist_maxvalue(head):
    temp = head
    maxValue = 0
    while temp is not None:
        if temp.value > maxValue:
            maxValue = temp.value
        temp = temp.next
    
    return maxValue

head = None
linklist = list(map(int,input().split()))

for value in linklist:
    if value == -1:
        break
    head = insert_at_tail(head,value)

print(find_linklist_maxvalue(head))