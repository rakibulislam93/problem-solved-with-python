
arr = [1,3,-1,-3,5,3,6,7] #output [3,3,5,5,6,7]

k = 3
left = 0
max_array = []

for right in range(len(arr)):
    if right - left + 1 == k:
        max_num = max(arr[left:right+1])
        max_array.append(max_num)
        left += 1
    
print(max_array)