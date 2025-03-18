
n = input()

a = int(n[0])
b = int(n[1])

if b==0:
    print('YES')
elif a%b==0 or b%a == 0:
    print('YES')
else:
    print('NO')
