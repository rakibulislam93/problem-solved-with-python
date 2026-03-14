
n,m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

last_row = [matrix[n-1][i] for i in range(m)]
last_col = [matrix[j][m-1] for j in range(n)]



print(*last_row)
print(*last_col)