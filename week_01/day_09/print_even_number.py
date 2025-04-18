
# time and space complexity ----> O(n)
def fun(arr,n):
    i = 0
    if n<0:
        return
    if n%2==0:
        print(arr[n],end=' ')
    
    fun(arr,n-1)

n = int(input())
arr = list(map(int,input().split()))
fun(arr,(n-1))