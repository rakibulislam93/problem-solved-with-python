
# arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
# k = 5
# window_sum = sum(arr[:k])
# subarray_avg = [window_sum/k]
# left = 0
# for right in range(k,len(arr)):
#     window_sum += arr[right] - arr[left]
#     avg = window_sum/k
#     subarray_avg.append(avg)
#     left += 1
# print(subarray_avg)

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

window_sum = 0
subarray_avg = []

for i, num in enumerate(arr):
    
    window_sum += num
    if i >= k - 1:
        print(i,k-1)
        subarray_avg.append(window_sum / k)
        window_sum -= arr[i - k + 1]

print(subarray_avg)
