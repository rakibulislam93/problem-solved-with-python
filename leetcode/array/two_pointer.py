
arr = [1,2,3,4,5,6]
target = 6

# time complexity ---- > O(n^2)
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j] == target:
#             print(arr[i],arr[j])
#     print()
    

left = arr[0]
right = len(arr)-1

while left<right:
    curr_sum = arr[left] + arr[right]
    if curr_sum == target:
        print(arr[left],arr[right])
        break
    elif curr_sum < target:
        left+=1
    else:
        right-=1
