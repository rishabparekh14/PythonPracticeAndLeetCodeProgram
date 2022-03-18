import re


def findDisappearedNumbers(nums):
        
        # length = len(nums)
        # i =1
        # tempArr = []
        
        # while i!= len(nums)+1:
        #     if i not in nums:
        #         tempArr.append(i)
        #     i+= 1
        # return tempArr
        j= 0
        length = len(nums)
        nums = sorted(nums)
        nums = list(set(nums))
        nums.append(-1)
        appendCounter =0
        
        for i in range(1, length+1):
            if  i == nums[j]:
                j+=1
            elif i != nums[j]:
                nums.append(i)
                appendCounter +=1
        if nums[-1] == -1:
            nums.pop()
        if appendCounter == 0:
            return []
        return nums[-appendCounter:]


        

#numbers = [4,3,2,7,8,2,3,1]
numbers = [1,2]
#[7,1,14,11]
#[-20,8,-6,-14,0,-19,14,4]
result = findDisappearedNumbers(numbers)
print(result)