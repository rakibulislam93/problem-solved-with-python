
n = int(input())
arr = list(map(int,input().split()))

def count_befor_one(arr:list[int], n:int)->int:
    count = 0
    
    for i in range(n):
        if arr[i] == 1:
            break
        count += 1
    return count

print(count_befor_one(arr, n))