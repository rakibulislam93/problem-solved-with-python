

# time and space complexity ---- > O(n)

t = int(input())

for _ in range(t):
    number = list(map(int,input()))
    mid = int(len(number)/2)
    leftSum = sum(number[:mid])
    rightSum = sum(number[-3:])

    print('YES' if leftSum==rightSum else 'NO')