
# time complexity ----> O(n^2)
# space complexity -----> O(1)
n = int(input())

for i in range(1,n+1):
    for space in range(n-i):
        print(' ',end='')
    
    for star in range((2*i)-1):
        print('*',end='')
    print()

for j in range(n,0,-1):
    for space in range(n-j):
        print(' ',end='')
        
    for star in range((2*j)-1):
        print('*',end='')
    print()