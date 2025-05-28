
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        

class myQueue:
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
        if not self.empty():
            self.sz -=1
            delNode = self.head
            delNode.prev = None
            self.head = delNode.next           
            del delNode

    def top(self):
        if not self.empty():
            return self.head.value
        
        return None
        
    def empty(self):
        return self.sz == 0


queue = myQueue()
new_queue = list(map(int,input().split()))
for value in new_queue:
    queue.push(value)

while not queue.empty():
    print(queue.top(),end=' ')
    queue.pop()


# time and space complexity --- O(n) but per operation takes O(1)