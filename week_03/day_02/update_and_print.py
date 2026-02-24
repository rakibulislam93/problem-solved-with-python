
n = int(input("Enter a number: "))
arr = list(map(int, input().split()))
x,y = map(int, input().split())
arr[x] = y

print(*arr[::-1])