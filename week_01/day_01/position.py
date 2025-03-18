
n = int(input())

arr = list(map(int,input().split()))

for index,value in enumerate(arr):
    if value <= 10:
        print(f'A[{index}] = {value}')
    