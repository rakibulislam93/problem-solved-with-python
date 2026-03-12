
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
x = int(input())

find = False

for i in range(n):
    for j in range(m):
        if matrix[i][j] == x:
            find = True
            break
    if find:
        break


print("will not take number" if find else "will take number")
