
test_case = int(input())


for _ in range(test_case):
    my_str = input()
    if len(my_str)>10:
        print(f'{my_str[0]}{len(my_str)-2}{my_str[-1]}')
    else:
        print(my_str)