
nums = [0,1,0,3,12]
left = 0
for right in range(len(nums)):
    if nums[right]!=0:
        nums[left],nums[right] = nums[right],nums[left]
        left+=1 
    print()