
# time and space complexity -----> O(n^2)

n = int(input())
matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
sum1 = 0
sum2 = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sum1 += matrix[i][j]
            
        if i+j==n-1:
            sum2 += matrix[i][(n-i)-1]

# result = (sum1-sum2)* -1
result = abs(sum1-sum2)
print(result)