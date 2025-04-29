
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def insert_at_tail(head,value):
    newNode = Node(value)
    if head == None:
        head = newNode
        return head

    temp = head
    while temp.next != None:
        temp = temp.next 
    
    temp.next = newNode
    
    return head

def show_list(head):
    temp = head
    while temp != None:
        print(temp.data,end=' ')
        temp = temp.next 
    
    print()

def insert_at_position(head,pos,value):
    newNode = Node(value)
    temp = head
    for i in range(pos-1):
        temp = temp.next 
    
    newNode.next = temp.next 
    temp.next = newNode

head = None

# head = insert_at_tail(head, 10)
# head = insert_at_tail(head, 20)
# head = insert_at_tail(head, 30)
# head = insert_at_tail(head, 40)

# show_list(head)
# insert_at_position(head,2,500)
# show_list(head)

while True:
    print('1. Insert value at tail')
    print('2. Show link list')
    print('3. Insert value at position ')
    print('4. exit')
    
    choice = input()
    if choice == '1':
        value = int(input('Enter the value : '))
        head = insert_at_tail(head,value)
        
    elif choice == '2':
        
        show_list(head)
        
    elif choice == '3':
        pos = int(input('Enter the position : '))
        value = int(input('Enter the value : '))
        insert_at_position(head,pos,value)
    
    else:
        break
        