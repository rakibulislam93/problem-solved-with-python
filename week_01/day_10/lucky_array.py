
# time and space complexity ----- > O(n)
n = int(input())
arr = list(map(int, input().split()))
min_val = min(arr)

count = arr.count(min_val)

print('Lucky' if count % 2 != 0 else 'Unlucky')