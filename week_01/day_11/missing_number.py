
# time complexity ----- > O(t)
# space complexity -----> O(1)
t = int(input())

for _ in range(t):
    m , a , b , c = map(int,input().split())

    missing_value = int(m/(a*b*c))

    if m == a*b*c*missing_value:
        print(missing_value)
    else:
        print(-1)