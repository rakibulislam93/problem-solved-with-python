

# time complexity ---- > O(t*n)
# space complexity -----> O(n)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    even_count = 0
    odd_count = 0

    if n % 2 != 0:
        print('-1')
        continue
    else:
        for num in arr:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        difference = abs(even_count - odd_count)
        print(difference // 2)