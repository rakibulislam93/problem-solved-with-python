
n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
main_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(n):
    for j in range(n):
        if i == j:
            main_diagonal_sum += matrix[i][j]
        
        if i + j == n - 1:
            secondary_diagonal_sum += matrix[i][j]

result = abs(main_diagonal_sum - secondary_diagonal_sum)
print(result)
