
arr = [50, 2, 5, 3, 10, 2]
k = 3

window_sum = sum(arr[:3])
max_sum = window_sum
left = 0
subarry = arr[:3]

for right in range(k,len(arr)):
    window_sum += arr[right] - arr[left]
    left += 1
    if window_sum > max_sum:
        max_sum = window_sum
        subarry = arr[left:right+1]

print(max_sum)
print(subarry)