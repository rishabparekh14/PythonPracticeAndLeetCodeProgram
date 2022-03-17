def thirdMax( nums):
    tempArr = []
        
    nums = set(nums)
        
    maxNumber = max(nums)
        
    if len(nums) < 3:
        return max(nums)
        
    nums.remove(maxNumber)
    secondMax = max(nums)
    nums.remove(secondMax)
    return max(nums)

numbers = [2,2,3,1]
result = thirdMax(numbers)
print(result)