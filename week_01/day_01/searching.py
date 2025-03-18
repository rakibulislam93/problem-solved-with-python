
n = int(input())
arr = list(map(int,input().split()))
x = int(input())

find_index = -1

for index , num in enumerate(arr):
    
    if num == x:
        find_index = index
        break

print(find_index)