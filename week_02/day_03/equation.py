
# time complexity ---- O(n log n) because use (pow )
# space complexity -----> O(1)
x , n = map(int,input().split())

result = 0
for i in range(n+1):
    if i%2==0:
        result += pow(x,i)

print(result-1)