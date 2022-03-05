from unittest import result


def sortedSquares(self, nums):
        for i in range(0, len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums
    
numbers = [-4,-1,0,3,10]
result = sortedSquares(numbers)
    
# class Solution(object):
#     def sortedSquares(self, A):
#         return sorted(x*x for x in A)
        