
"""
    #    
   ---   
  #####  
 ------- 
#########
 ------- 
  #####  
   ---   
    # 
"""

n = int(input())

space = n - 1
hash = 1
dash = 1

for i in range(1, n+1):
    for j in range(1, space + 1):
        print(" ", end="")
    
    if i%2==1:
        for k in range(1, hash + 1):
            print("#", end="")
    else:
        for l in range(1, dash + 1):
            print("-", end="")

    print()
    space -= 1
    hash += 2
    dash += 2

for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    
    if i%2==1:
        for k in range(1, 2*i):
            print("#", end="")
    else:
        for l in range(1, 2*i):
            print("-", end="")

    print()
    