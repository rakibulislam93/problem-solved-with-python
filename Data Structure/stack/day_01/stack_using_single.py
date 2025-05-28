
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class myStack:
    def __init__(self):
        self.head = None
        self.sz = 0
    
    def push(self,value):
        self.sz +=1
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode
    
    def pop(self):
        self.sz -=1
        if not self.empty():
            delNode = self.head
            self.head = delNode.next
            del delNode
    
    def top(self):
        if not self.empty():
            print(self.head.value,end=' ')
    
    
    
    def empty(self):
        return self.sz == 0

st = myStack()
new_stack = list(map(int,input().split()))
for value in new_stack:
    st.push(value)


while not st.empty():
    st.top()
    st.pop()