
m,a,b,c = map(int, input().split())

d = m / (a*b*c)
if d.is_integer():
    print(int(d))
else:
    print(-1)