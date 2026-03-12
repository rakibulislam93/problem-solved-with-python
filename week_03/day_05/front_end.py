
n = int(input())
arr = list(map(int, input().split()))
i = 0
j = len(arr) - 1
newarr = []
while i < j:
    newarr.append(arr[i])
    newarr.append(arr[j])
    i += 1
    j -= 1

if i == j:
    newarr.append(arr[i])

print(*newarr)
