
# time complexity -----> O(n^2)
# space complexit -------> O(n)
n = int(input())

arr = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(*arr)