
n,m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

flag = True

for i in range(n):
    for j in range(m):
        if i==j or i+j == m-1:
            if matrix[i][j] != 1:
                flag = False
                break
        else:
            if matrix[i][j] != 0:
                flag = False
                break

if flag:
    print("YES")
else:
    print("NO")
