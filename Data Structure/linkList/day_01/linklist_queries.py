
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

def linkListLength(head):
    count = 0
    temp = head
    while temp is not None:
        count +=1 
        temp = temp.next 
    return count

def print_linkList(head):
    temp = head
    while temp is not None:
        print(temp.value,end=" ")
        temp = temp.next 
    print()
        

def insert_at_position(head,pos,value):
    newNode = Node(value)
    if pos == 0:
        newNode.next = head
        head = newNode
        print_linkList(head)
        return head
    if pos > linkListLength(head):
        print('Invalid index')
        return head
    temp = head
    for i in range(pos-1):
        temp = temp.next 
    newNode.next = temp.next
    temp.next = newNode
    print_linkList(head)
    return head

head = None
linkList = list(map(int,input().split()))

for value in linkList:
    if value == -1:
        break
    head = insert_at_tail(head,value)

while True:
    print("1. Insert value at position")
    print("2. Exit")
    choice = input('Enter your choice : ')
    if choice == '1':
        index,value = map(int,input().split())
        head = insert_at_position(head,index,value)
        
    else:
        break
    