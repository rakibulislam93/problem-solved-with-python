
n = int(input())

line = 2*n-1
space = n-1
star = 1

for i in range(line):
    
    for j in range(space):
        print(' ',end='')
    
    for k in range(star):
        print('*',end='')
    
    if i<n-1:
        space -=1
        star +=2
    else:
        space +=1
        star -=2
    print()