

# time complexity ---- > O(n^2)
# space complexity ------> O(n)

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int,input().split()))
    min_result = float('inf')
    for i in range(n):
        for j in range(i+1,n):
            result = arr[i]+arr[j]+(j-i)
            if result < min_result:
                min_result = result

    print(min_result)