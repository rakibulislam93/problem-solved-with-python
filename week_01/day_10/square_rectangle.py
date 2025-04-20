
# time complexity ------ > O(t)
# space complexity --------> O(1)
t = int(input())
for _ in range(t):
    weight,height = map(int,input().split())

    if weight==height:
        print('Square')
    else:
        print('Rectangle')