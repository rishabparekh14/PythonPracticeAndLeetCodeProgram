def removeDuplicates(nums):
    j= i = 0
    while i != len(nums):
        if i== len(nums)-1:
            for k in range(j+1, len(nums)):
                nums[k] = "#"
        elif nums[i] != nums[i+1]:
            nums[j+1] = nums[i+1]
            j += 1
        
        i+= 1
    return j+1

        
            

        
        
            
    

#numbers = [1,1,2]
numbers = [0,0,1,1,1,2,2,3,3,4]
#[7,1,14,11]
#[-20,8,-6,-14,0,-19,14,4]
result = removeDuplicates(numbers)
print(result)

        