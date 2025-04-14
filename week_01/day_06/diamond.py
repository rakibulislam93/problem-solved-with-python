
"""
  *
 ***
*****
 ***
  *
  
"""

n = int(input())

for i in range(1,n+1):
    space_count = n-i
    star_count = 2*i - 1
    
    print(' ' * space_count + '*' * star_count)

for i in range(n-1,0,-1):
    space_count = n-i
    star_count = 2*i - 1
    
    print(' ' * space_count + '*' * star_count)
    