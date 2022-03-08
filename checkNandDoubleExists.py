def checkIfExist(arr):

    for i in range(len(arr)):
            if (arr[i]*2 in arr[i+1:]) or (arr[i]/2 in arr[i+1:]):
                return True
    return False

numbers = [-20,8,-6,-14,0,-19,14,4]
#[7,1,14,11]
#[-20,8,-6,-14,0,-19,14,4]
result = checkIfExist(numbers)
print(result)
        