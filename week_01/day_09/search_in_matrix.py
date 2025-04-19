# time and space complexity ---- > O(n*m)
 
n,m = map(int,input().split())
 
matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
 
value = int(input())
found = False
for row in matrix:
    if value in row:
        found = True
        break
 
print('will not take number' if found==True else 'will take number' )