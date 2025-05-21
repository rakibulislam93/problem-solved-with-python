
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

def display_value_normary(head):
    temp = head
    while temp:
        print(temp.value,end=' ')
        temp = temp.next 
    print()

def display_value_reverse(tail):
    temp = tail
    while temp:
        print(temp.value,end=' ')
        temp = temp.prev 
    print()


head = None
tail = None
linklist = list(input().split())
for value in linklist:
    if value == 'end':
        break
    head, tail = insert_at_tail(head,tail,value)

# display_value_normary(head)
# display_value_reverse(tail)

t = int(input())
for _ in range(t):
    cmnd = list(input().split())
    if cmnd[0]=="visit":
        if cmnd[1] in linklist:
            while head.value != cmnd[1]:
                head = head.next
            print(head.value)
        else:
            print('Not Available')
    elif cmnd[0] == 'prev':
        if head.prev:
            head = head.prev
            print(head.value)
        else:
            print('Not Available')
    elif cmnd[0] == 'next':
        if head.next:
            head = head.next
            print(head.value)
        else:
            print('Not Available')
        