

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.prev = None


def insert_at_head(head,tail,value):
    newNode = Node(value)
    if head is None:
        head = newNode
        tail = newNode
        return head,tail
    
    newNode.next = head
    head.prev = newNode
    head = newNode
    
    return head,tail

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

def insert_at_position(head,pos,value):
    newNode = Node(value)
    temp = head
    for i in range(pos-1):
        temp = temp.next
        
    newNode.next = temp.next
    temp.next.prev = newNode
    newNode.prev = temp
    temp.next = newNode
    
    return head

def linklist_length(head):
    count = 0
    temp = head
    while temp is not None:
        count +=1
        temp = temp.next
    return count

def print_normalway(head):
    temp = head
    while temp is not None:
        print(temp.value,end=' ')
        temp = temp.next 
    print()

def print_reverseway(tail):
    temp = tail 
    while temp is not None:
        print(temp.value,end=' ')
        temp = temp.prev 
    print()

head = None
tail = None


while True:
    print('1. Enter the position')
    print('2. Exit')
    choice = input()
    if choice == '1':
        
        pos = int(input('Enter the position : '))
        if pos==0:
            value = int(input('Enter the value : '))
            head,tail = insert_at_head(head,tail,value)
            print_normalway(head)
            print_reverseway(tail)
        elif pos == linklist_length(head):
            value = int(input('Enter the value : '))
            head,tail = insert_at_tail(head,tail,value)
            
            print_normalway(head)
            print_reverseway(tail)
            
        elif 0<pos and pos<linklist_length(head):
            value = int(input('Enter the value : '))
            head = insert_at_position(head,pos,value)
            
            print_normalway(head)
            print_reverseway(tail)
        else:
            print('Invalid position')
    else:
        break
        
