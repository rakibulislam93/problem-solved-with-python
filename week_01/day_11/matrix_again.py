
# time complexity ----- > O(n*m)
# space complexity -------> O(n+m)
n , m = map(int,input().split())
matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

last_row = matrix[-1]
last_col = [row[-1] for row in matrix]

# space complexity---- > O(n*m)
# for i in range(n):
#     for j in range(m):
#         if i==n-1:
#             last_row.append(matrix[i][j])
#         if j == m-1:
#             last_col.append(matrix[i][j])

print(*last_row)
print(*last_col)


