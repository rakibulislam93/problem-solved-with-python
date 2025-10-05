
arr = [2,5,7,4,8,6]
k = 3
window_sum = sum(arr[:3])
max_sum = window_sum

for i in range(k,len(arr)):
    window_sum += arr[i]-arr[i-k]
    max_sum = max(max_sum,window_sum)


print(max_sum)