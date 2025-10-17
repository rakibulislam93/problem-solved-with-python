
# arr = [1,2,5,7,4,3] target = 7

# arr = [1,2,5,7,4,3]
arr = [1,2,5,3]

target = 3
min_lenght = float('inf')
min_subarray = []
window_sum = 0
left = 0
for right in range(len(arr)):
    window_sum += arr[right]
    
    while window_sum >= target:
        cur_length = right - left + 1
        
        if cur_length<min_lenght:
            min_lenght = cur_length
        
            min_subarray = arr[left:right+1]
        
        
        window_sum -= arr[left]
        left += 1
        
        

print(min_lenght)
print(min_subarray)