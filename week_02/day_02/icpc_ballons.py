
# time complexity ---- > O(t*n)
# space complexity -----> O(n)
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    count = [0]*26

    for char in s:
        count[ord(char) - ord('A')] += 1

    total_bellon = 0

    for i in range(26):
        if count[i]>=1:
            total_bellon = total_bellon + 2 + (count[i]-1)

    print(total_bellon)