def sortedSquares( nums):
        
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums = sorted(nums)
        return nums

## Alternative approach given in leetcode
    # return sorted(x*x for x in A)

numbers = [-4,-1,0,3,10]
#[7,1,14,11]
#[-20,8,-6,-14,0,-19,14,4]
result = sortedSquares(numbers)
print(result)