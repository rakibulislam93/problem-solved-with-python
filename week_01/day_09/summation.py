
def fun(arr,n):
    total = 0
    
    if n<0:
        return 0
    
    return arr[n] + fun(arr,n-1)

n = int(input())
arr = list(map(int,input().split()))

print(fun(arr,n-1))