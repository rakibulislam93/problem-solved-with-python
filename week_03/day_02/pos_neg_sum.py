
n = int(input("Enter a number: "))
arr = list(map(int, input().split()))
pos_sum = 0
neg_sum = 0
for i in range(n):
    if arr[i] > 0:
        pos_sum += arr[i]
    else:
        neg_sum += arr[i]

print(pos_sum, neg_sum)


