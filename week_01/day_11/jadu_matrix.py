
# time and space complexity ----- > O(n*m)

n , m = map(int,input().split())
matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
    
flag = True
for i in range(n):
    for j in range(m):
        if i==j or i+j==m-1:
            if matrix[i][j]!=1:
                flag = False
                break      
        else:
            if matrix[i][j]!=0:
                flag = False
                break

print('YES' if flag else 'NO')