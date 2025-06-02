from collections import deque
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def input_tree():
    val = list(map(int,input().split()))
    if not val and val[0]==-1:
        return None
    
    root = Node(val[0])
    q = deque()    
    if root : q.append(root)
    
    indx = 1
    
    while q and indx<len(val):
        parentNode = q.popleft()
        # leftchild connection 
        
        if indx<len(val) and val[indx]!=-1:
            leftChild = Node(val[indx])
            parentNode.left = leftChild
            q.append(leftChild)
        
        indx +=1
        
        if indx<len(val) and val[indx]!=-1:
            rightChild = Node(val[indx])
            parentNode.right = rightChild
            q.append(rightChild)
        
        indx +=1
    
    return root
        

def level_order(root):
    q = deque()
    q.append(root)
    while q:
        node = q[0]
        q.popleft()
        print(node.value,end=' ')
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)      
        
        
root = input_tree()
level_order(root)