
n = int(input())

for i in range(1,n+1):
    
    for space in range(n-i):
        
        print(' ',end='')
    
    if i%2==0:
        for star in range((2*i)-1):
            print('-',end='')
    else:
        for dash in range((2*i)-1):
            print('#',end='')
    print()

for i in range(n-1,0,-1):
    for space in range(n-i):
        print(' ',end='')
    
    if i%2==0:
        for dash in range((2*i)-1):
            print('-',end='')
    else:
        for star in range((2*i)-1):
            print('#',end='')
    print()