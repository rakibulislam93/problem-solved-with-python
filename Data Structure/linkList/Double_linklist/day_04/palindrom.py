
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def insert_at_tail(head,tail,value):
    newNode = Node(value)
    if head is None:
        head = newNode
        tail = newNode
        return head,tail
    tail.next = newNode
    tail = newNode
    return head,tail

def check_palindrome(head,cur):
    if head is None:
        return True
    
    ans = check_palindrome(head.next,cur) and cur[0].value == head.value
    cur[0] = cur[0].next
    return ans
        

head = None
tail = None
linklist = list(map(int,input().split()))
for value in linklist:
    if value == -1:
        break
    head,tail = insert_at_tail(head,tail,value)

cur = [head]
result = check_palindrome(head,cur)
print(result)