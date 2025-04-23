
a,s,b,q,c = input().split()
a,b,c = map(int,[a,b,c])


if a+b==c or a-b==c or a*b==c:
    print('Yes')

else:
    if s=='+':
        print(a+b)
    elif s=='-':
        print(a-b)
    else:
        print(a*b)
    