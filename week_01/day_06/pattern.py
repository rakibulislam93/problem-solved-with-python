
"""
****
***
**
*
"""
# time complexity ----> O(n*2)
# space complexity ---> O(1)
# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print('*',end='')
#     print()

n = int(input())
for i in range(n,0,-1):
    print('*' * i)