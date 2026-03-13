
n = int(input())
arr = list(map(int, input().split()))

# def func(i):
#     if i == n-1:
#         return arr[i]
    
#     return max(arr[i], func(i+1))

# print(func(0))

def func(i):
    if i == 0:
        return arr[i]
    return max(arr[i], func(i-1))

print(func(n-1))