
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


def inser_at_tail(head,tail,value):
    newNode = Node(value)
    if head is None:
        head = newNode
        tail = newNode
        return head,tail
    
    tail.next = newNode
    tail = newNode
    return head,tail

def display_list_value(head):
    temp = head
    while temp:
        print(temp.value,end=' ')
        temp = temp.next 
    print()

def remove_duplicate(head):
    i = head
    while i:
        prev = i
        j = i.next
        while j:
            if i.value == j.value:
                prev.next = j.next  # delete j
                j = j.next
            else:
                prev = j
                j = j.next
        i = i.next
    return head

head = None
tail = None
linklist = list(map(int,input().split()))
for value in linklist:
    if value == -1:
        break
    head,tail = inser_at_tail(head,tail,value)

display_list_value(head)
head = remove_duplicate(head)
display_list_value(head)
        