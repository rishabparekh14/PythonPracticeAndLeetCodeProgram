def moveZeroes(nums):
    length = len(nums)
    j =0
        
    if length ==1:
        return
        
    for i in range(0, length):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            j +=1
    return nums
    
        
        
        


numbers = [-1,0,1,0,3,12]
#[7,1,14,11]
#[-20,8,-6,-14,0,-19,14,4]
result = moveZeroes(numbers)
print(result)


