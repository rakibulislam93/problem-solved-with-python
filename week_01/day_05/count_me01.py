
# time complexity--> O(n)
# space complexity --> O(n)
n = int(input())
ans1,ans2 = 0,0

# arr = list(map(int,input().split()))
# for value in arr:
#     if value % 2==0:
#         ans1 +=1
#     elif value%3==0:
#         ans2 += 1

# optimize code and reduce space complexity--> O(1)

for value in (map(int,input().split())):
    if value%2==0:
        ans1 +=1
    elif value%3==0:
        ans2 +=1

print(ans1,ans2)