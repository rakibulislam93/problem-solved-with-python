
n = int(input())

if n>0:
    # for i in range(1,n+1):
    #     print(i,end=" ")
    
    # its print a list..
    list = [i for i in range(1,n+1)]
    
    # behind the since for loop kaj kortache..
    print(*range(1,n+1))
    
else:
    for i in range(n,1):
        print(i,end=' ')