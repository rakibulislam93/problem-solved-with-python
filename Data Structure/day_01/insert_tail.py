
def insert_at_tail(head,data):
    newNode = Node(data)
    if head == None:
        head = newNode
        return head
    
    temp = head
    while temp.next != None:
        temp = temp.next 
        
    temp.next = newNode
    return head

def print_linkList(head):
    
    temp = head
    while temp != None:
        print(temp.data)
        temp = temp.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = None
while True:
    print('1. Insert value at tail')
    print('2. print linkList')
    print('3. Exit')
    print('Please choice your option : ')
    choice = input()
    
    if choice == '1':
        data = int(input())
        head = insert_at_tail(head,data)
    elif choice == '2':
        print_linkList(head)
    
    else:
        break
