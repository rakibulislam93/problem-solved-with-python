
# n = int(input())
# arr = list(map(int, input().split()))

# arr = [x for x in arr if x != 0] + [0] * arr.count(0)
# print(*arr)

n = int(input())
arr = list(map(int, input().split()))

pos = 0
for i in range(n):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1
    
print(*arr)