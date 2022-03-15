def sortArrayByParity(nums):
        
        length = len(nums)
        j =0
        if length == 1:
            return nums
        
        for i in range(0, length):
            
            if nums[i] %2 ==0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j +=1
        return nums    

numbers = [3,1,2,4]
#[7,1,14,11]
#[-20,8,-6,-14,0,-19,14,4]
result = sortArrayByParity(numbers)
print(result)