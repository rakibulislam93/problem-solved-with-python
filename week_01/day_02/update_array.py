
n = int(input())

arr = list(map(int,input().split()))
index,value = map(int,input().split())

arr[index]=value

print(*arr[::-1])