
n = int(input())
arr = list(map(int,input().split()))

for index,value in enumerate(arr):
    if value>0:
        arr[index]=1
    elif value<0:
        arr[index] = 2
        

print(*arr)