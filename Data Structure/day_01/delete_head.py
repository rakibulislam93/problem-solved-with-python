
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

def length_linkList(head):
    temp = head
    count = 0
    while temp is not None:
        count +=1
        temp = temp.next 
    return count

def insert_at_opsition(head,pos,value):
    newNode = Node(value)
    
    if pos==0:
        print('Wow you insert head and value = ',value)
        newNode.next = head
        head = newNode
        return head

    temp = head
    
    if pos>0 and pos<length_linkList(head):
        print(f'Your insert position is {pos}')
        for i in range(pos-1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
    else:
        print('Position out of range..please choice valid position')
    
    return head

def delete_head(head):
    temp = head
    delNode = temp
    head = temp.next
    del delNode
    print(f'Now your head value {head.data}')
    return head

def show_linkList(head):
    temp = head
    while temp != None:
        print(temp.data,end=' ')
        temp = temp.next 
    print()


head = None

while True:
    print('1. Insert at position')
    print('2. Show link List ')
    print('3. Delete head node')
    print('4. exit')
    choice = input()
    if choice == '1':
        pos = int(input('Enter the postion : '))
        value = int(input('Enter the value : '))
        head = insert_at_opsition(head,pos,value)
    
    elif choice == '2':
        show_linkList(head)
    
    elif choice == '3':
        head = delete_head(head)
    else:
        break