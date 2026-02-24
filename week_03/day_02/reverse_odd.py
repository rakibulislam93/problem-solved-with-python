
# arr = list(map(int, input().split()))

# for i in range(len(arr)-1, -1, -1):
#     if i % 2 == 1:
#         print(arr[i], end=" ")

import sys
arr = list(map(int, sys.stdin.readline().split()))

print(*arr[-1::-2])