def removeElement(nums, val):
        i=0
        for j in range(0,len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i +=1
                print(nums)
        return i

numbers = [3,2,2,3]
result = removeElement(numbers,3)
print(result)