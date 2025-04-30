
class Node:
    def __init__(self,data):
        self.data = data
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

def length_linkList(head):
    count = 0;
    temp = head
    while temp!=None:
        count +=1
        temp = temp.next
    return count

def show_link_list(head):
    temp = head
    while temp is not None:
        print(temp.data,end=' ')
        temp = temp.next 
    print()

def insert_at_position(head,pos,value):
    newNode = Node(value)
    
    if pos == 0:
        print('Insert head = ',value)
        newNode.next = head
        head = newNode
        return head
    
    if pos>=length_linkList(head):
        print('position out of range...')
        return head
    
    temp = head
    
    for i in range(pos-1):
        temp = temp.next
    
    newNode.next = temp.next
    temp.next = newNode
    return head

def delete_at_position(head,pos):
    temp = head
    for i in range(pos-1):
        temp = temp.next
    
    delNode = temp.next
    temp.next = delNode.next
    del delNode
    
    return head

head = None

while True:
    print('1. Insert value at tail')
    print('2. Show link list')
    print('3. Insert value at position ')
    print('4. Delete value at position ')
    print('5. exit')
    
    choice = input()
    if choice == '1':
        value = int(input('Enter the value : '))
        head = insert_at_tail(head,value)
        
    elif choice == '2':
        
        show_link_list(head)
        
    elif choice == '3':
        pos = int(input('Enter the position : '))
        value = int(input('Enter the value : '))
        head = insert_at_position(head,pos,value)
    
    elif choice == '4':
        pos = int(input('Enter the position : '))
        head = delete_at_position(head,pos)
    
    else:
        break
        