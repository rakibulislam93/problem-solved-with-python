
# time complexity ----> O(n^2)
# space complexity -----> O(1)
n = int(input())

for i in range(1,n+1):
    # for print space 
    for space in range(n-i):
        print(' ',end='')
    
    # for print start '*'
    for star in range((2*i)-1):
        print('*',end='')
    print()