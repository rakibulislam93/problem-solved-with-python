
import sys
sys.setrecursionlimit(10000)

n = int(input())
arr = list(map(int, input().split()))

def recursive_sum(arr, i):
    if i == len(arr):
        return 0

    sum = arr[i] + recursive_sum(arr, i+1)
    return sum

print(recursive_sum(arr, 0))


