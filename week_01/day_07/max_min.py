
# time and space complexity ---- O(n)
def max_min(n,mylist):
    mx = mylist[0]
    mn = mylist[0]
    for i in range(n):
        if mylist[i]>mx:
            mx = mylist[i]
    for i in range(n):
        if mylist[i]<mn:
            mn = mylist[i]
    
    return mn,mx

n = int(input())
mylist = list(map(int,input().split()))

mn,mx = max_min(n,mylist)
print(mn,mx)
    
        