
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

def check_linklist_same_or_not(head1,head2):
    flag = True
    temp1 = head1
    temp2 = head2
    while temp1 is not None:
        if temp1.value != temp2.value:
            flag = False
            break
        temp1 = temp1.next 
        temp2 = temp2.next 
    return flag

head1 = None
tail1 = None
head2 = None
tail2 = None

linklist1 = list(map(int,input().split()))
linklist2 = list(map(int,input().split()))



for value in linklist1:
    if value == -1:
        break
    head1,tail1 = insert_at_tail(head1,tail1,value)

for value in linklist2:
    if value == -1:
        break
    head2,tail2 = insert_at_tail(head2,tail2,value)
if len(linklist1) != len(linklist2):
    print('NO')
else:
    result = check_linklist_same_or_not(head1,head2)

    print('YES' if result else 'NO')