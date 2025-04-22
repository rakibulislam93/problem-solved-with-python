
n = int(input())

line = n
space = 0
star = 2*n-1

for i in range(n):
    for j in range(space):
        print(' ',end='')
    
    for k in range(star):
        print('*',end='')
    
    space +=1
    star -=2
    print()