def removeDuplicates(nums):


    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
    print(nums)
    return i+1
        
        
        ## Using a new array approach

        # uniqueList = []
        # count = 0
        # for x in nums:
        #     if x not in uniqueList:
        #         uniqueList.append(x)
                
                
        # for i in range(0, len(uniqueList)-1):
        #     count = 0
        #     for rpi in range(0, len(nums)-1):
        #         if uniqueList[i] == nums[rpi]:
        #             count += 1
        #             if count > 1:
        #                 uniqueList.append(nums[rpi])
        # nums = uniqueList[:]
        # print("Sorted elements by pushing duplicates to end:",nums)
        # return len(nums)


numbers = [1,2]
result = removeDuplicates(numbers)
print(result)