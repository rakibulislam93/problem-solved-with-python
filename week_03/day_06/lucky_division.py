
n = int(input())

for i in range(1, n + 1):
    x = i
    lucky = True
    while x > 0:
        digit = x % 10
        if digit != 4 and digit != 7:
            lucky = False
            break
        x //= 10
    if lucky and n % i == 0:
        print("YES")
        break
else:    print("NO")