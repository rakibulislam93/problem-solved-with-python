
# time complexity ---- > O(n^2)
# space complexity -----> O(1)

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

def check_duplicate(head):
    temp = head
    count = [0]*101
    while temp is not None:
        count[temp.value]+=1
        temp = temp.next 
    
    return count


head = None
linkList = list(map(int,input().split()))

for value in linkList:
    if value == -1:
        break
    head = insert_at_tail(head,value)

linkList_counter = check_duplicate(head)

flag = False
for i in range(len(linkList_counter)):
    if linkList_counter[i]>1:
        flag = True
        break

print('YES' if flag else 'NO')