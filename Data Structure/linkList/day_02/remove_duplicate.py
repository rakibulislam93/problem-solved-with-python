
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        
def insert_at_tail(head,value):
    newNode = Node(value)
    if head is None:
        head = newNode
        return head

    temp =head
    while temp.next is not None:
        temp = temp.next 
    temp.next = newNode
    return head

def remove_duplicate(head):
    i = head
    
    while i.next is not None:
        j = i
        while j.next is not None:
            if i.value == j.next.value:
                delNode = j.next
                j.next = j.next.next 
                del delNode
            
            else:
                j = j.next 
            
        i = i.next
    
    

def print_linklist(head):
    temp = head
    while temp is not None:
        print(temp.value,end=" ")
        temp = temp.next 
    print()
    

head = None
linkList = list(map(int,input().split()))
for value in linkList:
    if value == -1:
        break
    head = insert_at_tail(head,value)
    

print_linklist(head)
remove_duplicate(head)
print_linklist(head)