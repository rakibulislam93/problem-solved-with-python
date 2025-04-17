
# time and space complexity ----> O(n)
def count_before_one(n,arr):
    count = 0
    for val in arr:
        if val != 1:
            count +=1
        else:
            if val == 1:
                break
    
    return count

n = int(input())
arr = list(map(int,input().split()))
print(count_before_one(n,arr))