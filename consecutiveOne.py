def findMaxConsecutiveOnes(nums):
        count =0
        consecutiveList = []
        for j in range(0,len(nums)):
            if nums[j] ==1:
                count +=1
            else:
                consecutiveList.append(count)
                count =0
                print(consecutiveList)
        consecutiveList.append(count)
        max = consecutiveList[0]
        for i in range(0, len(consecutiveList)):
            if consecutiveList[i] > max:
                max = consecutiveList[i]
        return max

        #  count = max_count = 0
        # for num in nums:
        #     if num == 1:
        #         # Increment the count of 1's by one.
        #         count += 1
        #     else:
        #         # Find the maximum till now.
        #         max_count = max(max_count, count)
        #         # Reset count of 1.
        #         count = 0
        # return max(max_count, count)

numbers = [1,1,0,1,1,1]
result = findMaxConsecutiveOnes(numbers)
print(result)