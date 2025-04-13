
# time complexity ---- > O(n)
# space complexity ------> O(n)
n = int(input())
arr = list(map(int,input().split()))
value = int(input())

print('YES' if value in arr else 'NO')
