
n = int(input("Enter a number: "))

if n > 0:
    [print(f"{i}") for i in range(1, n + 1)]
else:
    [print(f"{i}") for i in range(n,1)]