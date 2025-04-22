
n = int(input())

line = int((n - 1) / 2 + 6)

for i in range(line):  # i = 0 theke line-1 porjonto
    for j in range(line - i - 1):  # space komche
        print(' ', end='')

    for k in range(2 * i + 1):  # star barche
        print('*', end='')

    print()

space = 5
star = n

for i in range(5):
    # for j in range(space):
    #     print(' ',end='')
    
    # for k in range(n):
    #     print('*',end='')
    # print()

    total_space = ' '*space
    total_star = '*'*star
    
    print(total_space+total_star)
