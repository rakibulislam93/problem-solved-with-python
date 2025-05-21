
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

def insert_at_position(head,tail,pos,value):
    newNode = Node(value)
    if head is None:
        head = newNode
        tail = newNode
        return head,tail
    
    if pos == 0:
        newNode.next = head
        head.prev = newNode
        head = newNode
        return head,tail
    
    if pos == linklist_size(head):
        tail.next = newNode
        newNode.prev = tail
        tail = newNode
        return head,tail
    
    temp = head
    for _ in range(pos-1):
        temp = temp.next
        
    newNode.next = temp.next
    temp.next.prev = newNode
    newNode.prev = temp
    temp.next = newNode
        
    return head,tail

def linklist_size(head):
    temp = head
    count = 0
    while temp:
        count += 1
        temp = temp.next 
    return count

def display_linklist_value(head):
    print("L -> ",end=' ')
    temp = head
    while temp:
        print(temp.value,end=' ')
        temp = temp.next 
    print()

def display_linklist_reverse(tail):
    print("R -> ",end=' ')
    temp = tail
    while temp:
        print(temp.value,end=' ')
        temp = temp.prev
    print()

head = None
tail = None

t = int(input())
for _ in range(t):
    index,value = map(int,input().split())
    if index > linklist_size(head):
        print('Invalid')
    else:
        head,tail = insert_at_position(head,tail,index,value)
        display_linklist_value(head)
        display_linklist_reverse(tail)