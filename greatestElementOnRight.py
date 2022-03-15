from operator import indexOf


def replaceElements(arr):
    # Below code is correct but for larger inputs it is not efficient

    # indexOfBigElement = arr.index(max(arr))
    # i =rpi =0
    # length = len(arr)
    # while rpi < length:
    #     for k in range(i,indexOfBigElement):
    #         arr[k] = arr[indexOfBigElement]
    #     i = rpi = indexOfBigElement
    #     if rpi == length-1:
    #         arr[rpi] = -1
    #         break
    #     indexOfBigElement = arr.index(max(arr[i+1:])) 

    maxNumber = -1
    for i in range(len(arr)-1, -1 ,-1):
        arr[i], maxNumber = maxNumber , max(arr[i], maxNumber)
    return arr

numbers = [400]
#[7,1,14,11]
#[-20,8,-6,-14,0,-19,14,4]
result = replaceElements(numbers)
print(result)

        

        
        
