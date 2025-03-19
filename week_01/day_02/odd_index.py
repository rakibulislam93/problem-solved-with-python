
n = int(input())

arr = list(map(int,input().split()))

revlist = [arr[i] for i in range(n-1,-1,-1) if i%2 != 0]
print(*revlist)