
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

def count_linklist_length(head):
    count = 0
    temp = head
    while temp is not None:
        count +=1 
        temp = temp.next
    return count

head1 = None
head2 = None

linklist1 = list(map(int,input().split()))
linklist2 = list(map(int,input().split()))

for value in linklist1:
    if value == -1:
        break
    head1 = insert_at_tail(head1,value)

for value in linklist2:
    if value == -1:
        break
    head2 = insert_at_tail(head2,value)

count1 = count_linklist_length(head1)
count2 = count_linklist_length(head2)

print('YES' if count1==count2 else 'NO')
