
n = int(input())

def recursion(n):
    if n < 1:
        return
    recursion(n - 1)
    print(n)

recursion(n)

