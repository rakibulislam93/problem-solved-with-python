
def fun(n, c):
    for _ in range(n):
        print(c, end=' ')

t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)

    fun(n, c)
    print()