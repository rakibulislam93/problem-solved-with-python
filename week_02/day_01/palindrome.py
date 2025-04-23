
# time and space complexity ----> O(n)
n = int(input())
arr = list(map(int,input().split()))

i = 0
j = n-1
flag = True
while i<j:
    if arr[i]!=arr[j]:
        flag = False
        break
    i+=1
    j-=1
print('YES' if flag else 'NO')


# mid = int(len(arr)/2)

# j = n-1
# flag = True
# for i in range(mid):
#     if arr[i]!= arr[j]:
#         flag = False
#         break
#     j -= 1

# print('YES' if flag else 'NO')

    
    