
# time complexity ----- > O(n log n)
# space complexity -------> O(n)
n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
c = []

for i in range(n):
    value = abs(a[i]-b[i])
    c.append(value)

print(*c)
