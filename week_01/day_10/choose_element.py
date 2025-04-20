
# time complexity ---- > O(n log n)
# space complexity ------ > O(n)
n , k = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse=True)
max_sum = 0
for i in range(k):
    if arr[i]>0:
        max_sum += arr[i]
    else:
        break

print(max_sum)