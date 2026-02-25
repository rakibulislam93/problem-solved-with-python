
t = int(input())
for _ in range(t):

    m1,m2,d = map(int, input().split())
    result = (m1*d)//(m1+m2)
    print(d-result)