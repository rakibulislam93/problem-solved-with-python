
n = int(input())

for i in range(1,n+1):
    for space in range(n-i):
        print(' ',end='')
    
    for val in range(i,0,-1):
        print(val,end='')
        
    print()