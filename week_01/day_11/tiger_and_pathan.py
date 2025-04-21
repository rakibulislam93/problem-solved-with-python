
# time complexity ----- > O(t*n)
# space complexity -------> O(n)

t = int(input())
for _ in range(t):
    n = int(input())
    S = input()
    count_T = 0
    count_P = 0
    for char in S:
        if char == 'T' or char == 't':
            count_T += 1
        elif char == 'P' or char=='p':
            count_P += 1

    if count_T>count_P:
        print('Tiger')
    elif count_P>count_T:
        print('Pathaan')
    else:
        print('Draw')