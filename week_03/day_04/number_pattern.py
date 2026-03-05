
n = int(input())

space = n - 1
for i in range(1, n + 1):
    for j in range(1, space + 1):
        print(" ", end="")
    for k in range(i, 0, -1):
        print(k, end="")
    print()
    space -= 1
