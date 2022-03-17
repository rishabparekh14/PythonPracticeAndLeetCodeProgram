def removeElement(nums, val: int):
    i = 0
    length = len(nums)
    for j in range(0, len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i +=1
    return i