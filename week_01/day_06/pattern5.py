
"""
*******
 *****
  ***
   *
"""

n = int(input())

for i in range(n,0,-1):
    for space in range(n-i):
        print(' ',end='')
    
    for star in range((2*i)-1):
        print('*',end='')
    print()