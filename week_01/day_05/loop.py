
# time complexity ----> O(n*k)
# space complexity -----> O(1)

n,k = map(int,input().split())

# for _ in range(n):
    # for i in range(1,k+1):
    #     print(i,end=' ')
    # print()
for _ in range(n):
    print(*range(1, k+1))