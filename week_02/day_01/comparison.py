
a , s , b = input().split()
a = int(a)
b = int(b)

if a > b and s == '>':
    print('Right')
elif a < b and s == '<':
    print('Right')
elif a == b and s == '=':
    print('Right')
else:
    print('Wrong')