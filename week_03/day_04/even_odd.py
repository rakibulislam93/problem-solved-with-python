
def odd_even():
    n = int(input())
    arr = list(map(int, input().split()))
    even_count = 0
    odd_count = 0
    for val in arr:
        if val % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    print(even_count, odd_count)


odd_even()