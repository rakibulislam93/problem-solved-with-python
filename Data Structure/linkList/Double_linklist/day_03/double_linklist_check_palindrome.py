
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

def check_palindrome(head,tail):
    flag = True
    temp1 = head
    temp2 = tail
    
    while temp1 != temp2 and temp2.next != temp1 :
        if temp1.value != temp2.value:
            flag = False
            break
        temp1 = temp1.next 
        temp2 = temp2.prev
    
    return flag

head = None
tail = None

linklist = list(map(int,input().split()))
for value in linklist:
    if value == -1:
        break
    head,tail = insert_at_tail(head,tail,value)

result = check_palindrome(head,tail)

print('YES' if result else 'NO')