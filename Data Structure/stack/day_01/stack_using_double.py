
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class myStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0
    
    def push(self,value):
        self.sz +=1
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
    
    def pop(self):
        self.sz -=1
        if not self.empty():
            delNode = self.tail
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
    
    def top(self):
        print(self.tail.value,end=" ")
    
    def empty(self):
        return self.sz == 0
    

st = myStack()
new_stack = list(map(int,input().split()))

for value in new_stack:
    st.push(value)

while not st.empty():
    st.top()
    st.pop()