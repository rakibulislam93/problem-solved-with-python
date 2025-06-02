
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

def count_node(root):
    if root is None:return 0
    l = count_node(root.left)
    r = count_node(root.right)
    return l+r+1

 
root = input_tree()
print(count_node(root))