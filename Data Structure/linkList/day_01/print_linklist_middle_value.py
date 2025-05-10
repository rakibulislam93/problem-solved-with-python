
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

def linklist_length(head):
    count = 0
    temp = head
    while temp is not None:
        count +=1
        temp = temp.next 
    return count

def print_linklist_middleValue(head):
    linkListLength = linklist_length(head)
    temp = head
    print(linkListLength,"*********")
    if linkListLength % 2 !=0:
        for i in range(linkListLength//2):
            temp = temp.next
        print(temp.value)
    else:
        for i in range(1,linkListLength//2):
            temp = temp.next
        print(temp.value,temp.next.value)
    
    return head

head = None

linkList = map(int,input().split())

for value in linkList:
    if value == -1:
        break
    head = insert_at_tail(head,value)
    

print_linklist_middleValue(head)