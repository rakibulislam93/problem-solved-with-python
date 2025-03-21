

n = int(input())
arr = list(map(int,input().split()))

max_value = max(arr)
min_value = min(arr)


for index,value in enumerate(arr):
    if value == max_value:
        arr[index] = min_value
    if value == min_value:
        arr[index] = max_value
        
print(*arr)