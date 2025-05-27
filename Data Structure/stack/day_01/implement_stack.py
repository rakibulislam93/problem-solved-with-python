
class myStack:
    def __init__(self):
        self.stack = []
    
    def push(self,value):
        self.stack.append(value)
    
    def top(self):
        if not self.empty():
            print(self.stack[-1],end=' ')
    
    def pop(self):
        if not self.empty():
            self.stack.pop()
    
    def empty(self):
        return len(self.stack) == 0

st = myStack()
new_stack = list(map(int,input().split()))
for value in new_stack:
    st.push(value)

while not st.empty():
    st.top()
    st.pop()

